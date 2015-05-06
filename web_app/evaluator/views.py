from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Course, Professor, Student, StudentGroup
from .tasks import evaluate


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
