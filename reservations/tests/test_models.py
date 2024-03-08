from django.test import TestCase
from properties.models import Property
from advertisements.models import Advertisement
from ..models import Reservation
import datetime

class ReservationModelTest(TestCase):
    def test_reservation_creation(self):
        property = Property.objects.create(name="Beach House", address="123 Ocean View", description="Beautiful beach house.")
        ad = Advertisement.objects.create(property=property, platform_name="Airbnb", platform_fee=10.0)
        reservation = Reservation.objects.create(
            advertisement=ad,
            check_in=datetime.date.today(),
            check_out=datetime.date.today() + datetime.timedelta(days=1),
            total_price=200.0
        )
        self.assertTrue(isinstance(reservation, Reservation))