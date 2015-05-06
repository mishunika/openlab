from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Assignment, Course, Professor, Student, StudentGroup
from .tasks import evaluate
from .forms import SolutionSubmitForm


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        evaluate.delay(123321)
        return super(Dashboard, self).get(request, *args, **kwargs)


class Courses(ListView):
    queryset = Course.objects.all()
    template_name = "courses.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(Courses, self).get_queryset()
        student = Student.objects.filter(user=self.request.user)
        professor = Professor.objects.filter(user=self.request.user)
        if student:
            return queryset.filter(studentgroup__student=student)
        elif professor:
            return queryset.filter(professor=professor)

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

    def get_context_data(self, **kwargs):
        context = super(AssignmentView, self).get_context_data(**kwargs)
        context['form'] = SolutionSubmitForm
        return context
