from django.test import TestCase
from ..models import Property

class PropertyModelTest(TestCase):
    def test_property_creation(self):
        property = Property.objects.create(name="Beach House", address="123 Ocean View", description="Beautiful beach house.")
        self.assertTrue(isinstance(property, Property))
        self.assertEqual(property.__str__(), property.name)