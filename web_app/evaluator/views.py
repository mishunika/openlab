from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Course, Professor, Student, StudentGroup


class Dashboard(TemplateView):
    template_name = "dashboard.html"


class Courses(ListView):
    queryset = Course.objects.all()
    template_name = "courses.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(Courses, self).get_queryset()
        student = Student.objects.filter(user=self.request.user)
        professor = Professor.objects.filter(user=self.request.user)
        if student:
            c_student_group = StudentGroup.objects.filter(student=student)
            return queryset.filter(studentgroup=c_student_group)
        elif professor:
            return queryset.filter(professor=professor)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Courses, self).dispatch(*args, **kwargs)
