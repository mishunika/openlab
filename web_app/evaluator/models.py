import os
from hashlib import md5
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models


TESTS_PATH = os.path.dirname(os.path.abspath(__file__)) + '_tests'
TESTS_STORAGE = FileSystemStorage(location=TESTS_PATH)
SUBMISSIONS_PATH = os.path.dirname(os.path.abspath(__file__)) + '_submissions'
SUBMISSIONS_STORAGE = FileSystemStorage(location=SUBMISSIONS_PATH)

class Course(models.Model):
    STUDY_DEGREE = (
        ('B', 'Bachelor'),
        ('M', 'Master'),
    )

    title_en = models.CharField(max_length=64)
    title_ro = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    study_degree = models.CharField(
        max_length=1, choices=STUDY_DEGREE, default='B')
    ects = models.IntegerField(null=True)

    class Meta:
        unique_together = ('study_degree', 'code',)

    def __str__(self):
        return self.full_code()

    def full_code(self):
        return '-'.join([self.study_degree, self.code])
    full_code.short_description = "Full course code"


class Assignment(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()

    course = models.ForeignKey('Course')

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return ': '.join([self.course.full_code(), self.title])


class TestCase(models.Model):
    LANG = (
        ('P', 'Python'),
        ('R', 'Ruby'),
    )

    file = models.FileField(storage=TESTS_STORAGE)
    lang = models.CharField(max_length=1, choices=LANG, default='P')
    added = models.DateTimeField(auto_now_add=True)

    assignment = models.ForeignKey('Assignment')

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return ' '.join([self.get_lang_display(), self.assignment.full_name()])


class Submission(models.Model):
    STATUS = (
        ('N', 'New'),
        ('T', 'Testing'),
        ('P', 'Passed'),
        ('F', 'Failed'),
    )

    file = models.FileField(storage=SUBMISSIONS_STORAGE, null=True)
    added = models.DateTimeField(auto_now_add=True)
    score = models.PositiveSmallIntegerField()
    metadata = models.CharField(max_length=1024)
    status = models.CharField(max_length=1, choices=STATUS, default='N')

    assignment = models.ForeignKey('Assignment')
    student = models.ForeignKey('Student')

    def md5(self):
        return md5(self.file.name.encode('utf-8')).hexdigest()

class StudentGroup(models.Model):
    name = models.CharField(max_length=4)
    speciality = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    enrolled_courses = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '-'.join([self.name, str(self.number)])


class Professor(models.Model):
    user = models.OneToOneField(User)
    courses = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        courses_codes = map(lambda x: x.full_code(), self.courses.all())
        brief_info = [self.user.username, ', '.join(courses_codes)]
        return ': '.join(brief_info)


class Student(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey('StudentGroup', blank=True, null=True)

    def __str__(self):
        return ': '.join([self.group.full_name(), self.user.username])


class Feed(models.Model):
    assignment = models.ForeignKey('Assignment')
    professor = models.ForeignKey('Professor')
