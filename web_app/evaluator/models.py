from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    students = models.ManyToManyField('Student')
    professors = models.ManyToManyField('Professor')


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


class Professor(models.Model):
    user = models.OneToOneField(User)


class Student(models.Model):
    user = models.OneToOneField(User)
