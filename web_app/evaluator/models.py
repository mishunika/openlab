from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=64)
    code = models.CharField(max_length=3)


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
    name = models.CharField(max_length=16)
    enrolled_courses = models.ManyToManyField('Course', blank=True)


class Professor(models.Model):
    user = models.OneToOneField(User)
    courses = models.ManyToManyField('Course', blank=True)


class Student(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey('StudentGroup', blank=True, null=True)


class Feed(models.Model):
    assignment = models.ForeignKey('Assignment')
    professor = models.ForeignKey('Professor')
