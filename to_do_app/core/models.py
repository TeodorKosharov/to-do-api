from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    difficulty = models.CharField(max_length=10, choices=(
        ('1', 'easy'),
        ('2', 'medium'),
        ('3', 'hard')
    ), null=False, blank=False)
    priority = models.IntegerField(null=False, blank=False)
