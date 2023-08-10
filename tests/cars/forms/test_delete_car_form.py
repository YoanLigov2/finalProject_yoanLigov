from django.test import TestCase
from ligovAuto.car.forms import CarDeleteForm
from ligovAuto.car.models import Car
from ligovAuto.user_profile.models import CollectionUser


class CarFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for ForeignKey reference
        cls.user = CollectionUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='1234567890',
            password='testpassword'
        )

        cls.form_data = {
            'image': 'path/to/image.png',
            'car_type': 'Sports Car',
            'model': 'Porsche 911',
            'year': 2022,
            'fuel_type': 'Diesel',
            'top_speed': 250,
            'emission_standard': 'Euro V',
            'horse_power': 500,
            'price': 200000.0,
            'user': cls.user,
            'short_description': 'Test car description',
        }

    def test_car_delete_form_disabled_fields(self):
        form = CarDeleteForm(data=self.form_data)
        for field in form.fields.values():
            self.assertIn('disabled', field.widget.attrs)
            self.assertFalse(field.required)

    def test_car_delete_form_save(self):
        form = CarDeleteForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        form.clean()