
from django.db import models
from properties.models import Property
from django.core.exceptions import ValidationError
from django.utils import timezone

class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.start_date < timezone.now().date():
            raise ValidationError("The start date cannot be in the past.")
        if self.end_date <= self.start_date:
            raise ValidationError("The end date must be after the start date.")

    def __str__(self):
        return f"Reservation at {self.property.name} from {self.start_date} to {self.end_date}"
