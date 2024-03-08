from rest_framework import serializers
from .models import Advertisement
from properties.serializers import PropertySerializer

class AdvertisementSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'property', 'title', 'price']
