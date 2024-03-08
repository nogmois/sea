from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Property
from django.test import TestCase

class PropertyViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.property_data = {'name': 'Beach House', 'address': '123 Ocean View', 'description': 'Beautiful beach house.'}
        self.response = self.client.post(
            reverse('property-list'),
            self.property_data,
            format="json")

    def test_api_can_create_property(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)