from django.db import models
from django.contrib.auth.models import User


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


class Submission(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    score = models.PositiveSmallIntegerField()
    metadata = models.CharField(max_length=1024)

    assignment = models.ForeignKey('Assignment')
    student = models.ForeignKey('Student')


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


class Student(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey('StudentGroup', blank=True, null=True)

    def __str__(self):
        return ': '.join([self.group.full_name(), self.user.username])


class Feed(models.Model):
    assignment = models.ForeignKey('Assignment')
    professor = models.ForeignKey('Professor')
