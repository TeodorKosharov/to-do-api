from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    difficulty = models.CharField(max_length=10, choices=(
        ('easy', '1'),
        ('medium', '2'),
        ('hard', '3')
    ), null=False, blank=False)
    priority = models.IntegerField(null=False, blank=False)
