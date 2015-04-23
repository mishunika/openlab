from django.contrib import admin
from .models import Assignment
from .models import Course
from .models import Professor
from .models import Student
from .models import StudentGroup


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_ro', 'full_code')
    ordering = ('title_en',)


admin.site.register(Professor)
admin.site.register(Student)

admin.site.register(StudentGroup)
admin.site.register(Assignment)
