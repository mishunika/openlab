from django.contrib import admin
from .models import Assignment
from .models import Course
from .models import Professor
from .models import Student
from .models import StudentGroup


admin.site.register(Professor)
admin.site.register(Student)

admin.site.register(StudentGroup)
admin.site.register(Course)
admin.site.register(Assignment)
