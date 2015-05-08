from django.contrib import admin
from django.db.models.fields import TextField
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
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

@admin.register(Assignment)
class AssignmentAdmin(MarkdownModelAdmin):
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(TestCase)
