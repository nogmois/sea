# advertisements/models.py
from django.db import models
from properties.models import Property

class Advertisement(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
