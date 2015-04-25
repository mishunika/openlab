from django.views import generic
from .models import Course, Professor, Student, StudentGroup


class Dashboard(generic.TemplateView):
    template_name = "dashboard.html"


class Courses(generic.ListView):
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
