from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Reservation
from advertisements.models import Advertisement
from properties.models import Property
from django.test import TestCase
import datetime

class ReservationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.property = Property.objects.create(name="Beach House", address="123 Ocean View", description="Beautiful beach house.")
        self.ad = Advertisement.objects.create(property=self.property, platform_name="Airbnb", platform_fee=10.0)
        self.reservation_data = {
            'advertisement': self.ad.id,
            'check_in': datetime.date.today(),
            'check_out': datetime.date.today() + datetime.timedelta(days=1),
            'total_price': 200.0
        }
        self.response = self.client.post(
            reverse('reservation-list'),
            self.reservation_data,
            format="json")

    def test_api_can_create_reservation(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)