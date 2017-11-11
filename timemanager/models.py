from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.OneToOneField(User, null=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_start = models.DateTimeField('started')
    time_end = models.DateTimeField('ended', null = True, blank = True)
