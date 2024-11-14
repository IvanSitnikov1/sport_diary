from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    rep = models.CharField(max_length=100, null=True, blank=True)

    day = models.ForeignKey(
        'Day', on_delete=models.CASCADE, related_name='exercises'
    )


class Day(models.Model):
    comment = models.TextField()
    date = models.DateField(default=datetime.today())

    program = models.ForeignKey(
        'Program', on_delete=models.CASCADE, related_name='days'
    )


class Program(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='programs'
    )
