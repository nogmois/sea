from django.test import TestCase
from properties.models import Property
from ..models import Advertisement

class AdvertisementModelTest(TestCase):
    def test_advertisement_creation(self):
        property = Property.objects.create(name="Beach House", address="123 Ocean View", description="Beautiful beach house.")
        ad = Advertisement.objects.create(property=property, platform_name="Airbnb", platform_fee=10.0)
        self.assertTrue(isinstance(ad, Advertisement))
        self.assertEqual(ad.__str__(), ad.platform_name)