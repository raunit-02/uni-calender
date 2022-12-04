from django.db import models

class AdminEvents(models.Model):
    event_name = models.CharField(max_length=200)
    department = models.CharField(max_length=75)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()