from django.test import TestCase
from ligovAuto.car.forms import CarForm
from ligovAuto.user_profile.models import CollectionUser


class CarFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CollectionUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='1234567890',
            password='testpassword'
        )

        cls.invalid_form_data = {
            'image': 'path/to/image.png',
            'car_type': 'Sports Car',
            'model': 'Porsche 911',
            'year': 1,
            'fuel_type': 'Diesel',
            'top_speed': 1,
            'emission_standard': 'Euro V',
            'horse_power': 1,
            'price': 1,
            'user': cls.user,
            'short_description': 'Test car description',
        }

    def test_form_invalid_data(self):
        form = CarForm(self.invalid_form_data)
        self.assertFalse(form.is_valid())

