from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='programs',
    )


class Day(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, related_name='days',
    )


class Exercise(models.Model):
    name = models.CharField(max_length=50)

    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name='exercises'
    )


class Workout(models.Model):
    date = models.DateField(default=date.today())
    rep = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField()

    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name='workouts',
    )
