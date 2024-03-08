from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Advertisement
from django.test import TestCase
from properties.models import Property

class AdvertisementViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.property = Property.objects.create(name="Beach House", address="123 Ocean View", description="Beautiful beach house.")
        self.ad_data = {'property': self.property.id, 'platform_name': 'Airbnb', 'platform_fee': 10.0}
        self.response = self.client.post(
            reverse('advertisement-list'),
            self.ad_data,
            format="json")

    def test_api_can_create_advertisement(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)