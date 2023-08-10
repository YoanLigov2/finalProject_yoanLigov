from django.test import TestCase

from ligovAuto.car.models import Car
from ligovAuto.user_profile.models import CollectionUser


class CarModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for ForeignKey reference
        cls.user = CollectionUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='1234567890',
            password='testpassword'
        )

        # Create a car instance
        cls.car = Car.objects.create(
            image='path/to/image.jpg',
            car_type='Sports Car',
            model='Porsche 911',
            year=2022,
            fuel_type='Diesel',
            top_speed=250,
            emission_standard='Euro V',
            horse_power=500,
            price=200000.0,
            user=cls.user,
            short_description='Test car description'
        )

    def test_model_fields(self):
        # Check if model fields are correctly defined
        car = self.car
        self.assertEqual(car.image, 'path/to/image.jpg')
        self.assertEqual(car.car_type, 'Sports Car')
        self.assertEqual(car.model, 'Porsche 911')
        self.assertEqual(car.year, 2022)
        self.assertEqual(car.fuel_type, 'Diesel')
        self.assertEqual(car.top_speed, 250)
        self.assertEqual(car.emission_standard, 'Euro V')
        self.assertEqual(car.horse_power, 500)
        self.assertEqual(car.price, 200000.0)
        self.assertEqual(car.user, self.user)
        self.assertEqual(car.short_description, 'Test car description')

    def test_str_method(self):
        # Check if __str__() method returns the expected string representation
        car = self.car
        expected_str = f'{car.model}#{car.pk}'
        self.assertEqual(str(car), expected_str)


