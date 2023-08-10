from django.test import TestCase

from ligovAuto.truck.models import Truck
from ligovAuto.user_profile.models import CollectionUser


class TruckModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for ForeignKey reference
        cls.user = CollectionUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='1234567890',
            password='testpassword'
        )

        # Create a truck instance
        cls.truck = Truck.objects.create(
            image='path/to/image.jpg',
            model='Man',
            year=2022,
            truck_mass=5000.0,
            truck_height=3.8,
            engine_power=300.0,
            price=150000.0,
            user=cls.user,
            very_short_description='Test truck description'
        )

    def test_model_fields(self):
        # Check if model fields are correctly defined
        truck = self.truck
        self.assertEqual(truck.image, 'path/to/image.jpg')
        self.assertEqual(truck.model, 'Man')
        self.assertEqual(truck.year, 2022)
        self.assertEqual(truck.truck_mass, 5000.0)
        self.assertEqual(truck.truck_height, 3.8)
        self.assertEqual(truck.engine_power, 300.0)
        self.assertEqual(truck.price, 150000.0)
        self.assertEqual(truck.user, self.user)
        self.assertEqual(truck.very_short_description, 'Test truck description')

    def test_str_method(self):
        # Check if __str__() method returns the expected string representation
        truck = self.truck
        expected_str = f'{truck.model}#{truck.pk}'
        self.assertEqual(str(truck), expected_str)