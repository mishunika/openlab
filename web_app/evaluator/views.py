from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import View
from .forms import SolutionSubmitForm
from .models import Assignment
from .models import Course
from .models import Professor
from .models import Student
from .models import StudentGroup
from .models import Submission
from .tasks import evaluate


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        return super(Dashboard, self).get(request, *args, **kwargs)


class Courses(ListView):
    queryset = Course.objects
    template_name = "courses.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(Courses, self).get_queryset()
        student = Student.objects.filter(user=self.request.user)
        if student:
            return queryset.filter(studentgroup__student=student)
        else:
            return queryset.filter(professor__user=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Courses, self).dispatch(*args, **kwargs)


class AssignmentsListView(ListView):
    queryset = Assignment.objects
    template_name = "course_assignments.html"

    def get_queryset(self):
        queryset = super(AssignmentsListView, self).get_queryset()
        try:
            return queryset.filter(course_id=self.kwargs['id'])
        except KeyError:
            return queryset.filter(
                course__studentgroup__student__user=self.request.user)


class AssignmentView(DetailView):
    queryset = Assignment.objects
    template_name = "assignment_details.html"
    assignment_id = 0

    def get(self, request, *args, **kwargs):
        self.assignment_id = kwargs['pk']
        return super(AssignmentView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AssignmentView, self).get_context_data(**kwargs)
        context['form'] = SolutionSubmitForm
        context['assignment_id'] = self.assignment_id
        return context


class SolutionSubmitView(View):
    form_class = SolutionSubmitForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            submission_id = self.create_submission(kwargs['id'],
                                                   request.FILES.get(
                                                       'solution', None))

            # Pass the task to the RabbitMQ
            evaluate.delay(submission_id)
            return redirect(reverse_lazy('assignment_details',
                                         kwargs={'pk': kwargs['id']}))
        else:
            return None

    def create_submission(self, assignment_id, file):
        """
        This method creates the Submission entity and returns its id
        :param assignment_id: The id of the assignment for which the solution
        is provided
        :param file: solution source file
        :return: Submission id
        """
        student = Student.objects.get(user=self.request.user)
        assignment = Assignment.objects.get(id=assignment_id)

        # Create a new Submission entity
        submission = Submission(file=file,
                                score=0,
                                metadata='',
                                assignment=assignment,
                                student=student)
        submission.save()
        return submission.id
