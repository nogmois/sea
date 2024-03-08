from rest_framework import serializers
from .models import Reservation
from properties.serializers import PropertySerializer

class ReservationSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'property', 'start_date', 'end_date']
