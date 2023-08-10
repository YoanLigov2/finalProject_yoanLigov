from django.test import TestCase

from ligovAuto.motorbike.models import Motorbike
from ligovAuto.user_profile.models import CollectionUser


class MotorbikeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for ForeignKey reference
        cls.user = CollectionUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='1234567890',
            password='testpassword'
        )

        # Create a motorbike instance
        cls.motorbike = Motorbike.objects.create(
            image='path/to/image.jpg',
            bike_type='Scooter',
            model='Test Model',
            year=2022,
            engine_size=150,
            fuel_capacity=5,
            fuel_type='Petrol',
            top_speed=100,
            emission_standard='Euro IV',
            price=10000.0,
            user=cls.user,
            short_description='Test motorbike description'
        )

    def test_model_fields(self):
        # Check if model fields are correctly defined
        motorbike = self.motorbike
        self.assertEqual(motorbike.bike_type, 'Scooter')
        self.assertEqual(motorbike.image, 'path/to/image.jpg')
        self.assertEqual(motorbike.model, 'Test Model')
        self.assertEqual(motorbike.year, 2022)
        self.assertEqual(motorbike.engine_size, 150)
        self.assertEqual(motorbike.fuel_capacity, 5)
        self.assertEqual(motorbike.fuel_type, 'Petrol')
        self.assertEqual(motorbike.top_speed, 100)
        self.assertEqual(motorbike.emission_standard, 'Euro IV')
        self.assertEqual(motorbike.price, 10000.0)
        self.assertEqual(motorbike.user, self.user)
        self.assertEqual(motorbike.short_description, 'Test motorbike description')

    def test_str_method(self):
        # Check if __str__() method returns the expected string representation
        motorbike = self.motorbike
        expected_str = f'{motorbike.model}#{motorbike.pk}'
        self.assertEqual(str(motorbike), expected_str)
