from django.test import TestCase
from finalProject.car.forms import CarForm
from finalProject.user_profile.models import CollectionUser


class TestCarForm(TestCase):

    VALID_USER_DATA = {
        'username': 'testusername2',
        'email': 'test3@test3.com',
        'phone_number': '0896207842',
        'password': 'Yoan1234',

    }

    INVALID_CAR_DATA = {
        'car_type': 'type',
        'model': '123456789123456789123456789123456789',
        'year': '2020',
        'fuel_type': 'fuel',
        'top_speed': '150',
        'emission_standard': 'standard 1',
        'horse_power': '99',
        'image': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/'
                 'car-reviews/first-drives/legacy/10-porsche-718-cayman-gt4-rs-top-10.jpg?itok=BacF-43A',
        'price': '50',
    }

    VALID_CAR_DATA = {
        'car_type': 'Sports Car',
        'model': 'BMW',
        'year': '2000',
        'fuel_type': 'Diesel',
        'top_speed': '240',
        'emission_standard': 'Euro I',
        'horse_power': '120',
        'image': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/'
                 'car-reviews/first-drives/legacy/10-porsche-718-cayman-gt4-rs-top-10.jpg?itok=BacF-43A',
        'price': '1200',
    }

    def test_form_valid_with_valid_data(self):
        user = CollectionUser.objects.create(**self.VALID_USER_DATA)
        form = CarForm(self.VALID_CAR_DATA, user)

        self.assertTrue(form.is_valid())

    def test_form_valid_with_invalid_xxxx(self):
        user = CollectionUser.objects.create(**self.VALID_USER_DATA)
        form = CarForm(self.INVALID_CAR_DATA, user)

        self.assertFalse(form.is_valid())

