from django.db import models


class Priority(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, default=2)
