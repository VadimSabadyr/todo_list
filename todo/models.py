from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Task(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    complete = models.BooleanField(default=False, blank=True)
