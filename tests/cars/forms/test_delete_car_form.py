from django.test import TestCase
from finalProject.car.forms import CarDeleteForm
from finalProject.car.models import Car
from finalProject.user_profile.models import CollectionUser


class TestDeleteCarForm(TestCase):

    VALID_USER_DATA = {
        'username': 'testusername2',
        'email': 'test3@test3.com',
        'phone_number': '0896207842',
        'password': 'Yoan1234',

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

    def test_delete_form(self):
        user = CollectionUser.objects.create(**self.VALID_USER_DATA)
        car = Car.objects.create(**self.VALID_CAR_DATA, user=user)
        form = CarDeleteForm(self.VALID_CAR_DATA, instance=car)

        self.assertTrue(form.is_valid())