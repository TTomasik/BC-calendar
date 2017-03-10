from django.db import models
from django.utils import timezone
from colorful.fields import RGBColorField




class Calendar(models.Model):
    calendar_name = models.CharField(max_length=128)

    def __str__(self):
        return self.calendar_name

class Tour(models.Model):
    name = models.CharField(null=False, max_length=128)
    destination = models.CharField(null=False, max_length=64)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=True)
    first_name = models.CharField(null=False, max_length=32)
    last_name = models.CharField(null=False, max_length=32)
    company = models.CharField(max_length=64, null=True, blank=True)
    phone = models.IntegerField(null=False, blank=False)
    date_of_entry = models.DateTimeField(null=False, default=timezone.now)
    color = RGBColorField(null=False)
    tour_calendar = models.ForeignKey(Calendar)

    @property
    def tour_length(self):
        length = (self.end_date - self.start_date).days
        return length

    def __str__(self):
        return self.name


