from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=100, blank=True, null=True)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events_attending', blank=True)

    def __str__(self):
        return self.title
