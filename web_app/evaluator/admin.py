from django.contrib import admin
from .models import Assignment, Course, Professor, Student, StudentGroup
from .models import TestCase


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_ro', 'full_code')
    ordering = ('title_en',)


admin.site.register(Professor)
admin.site.register(Student)


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'speciality')
    ordering = ('name', 'number')

admin.site.register(Assignment)
admin.site.register(TestCase)
