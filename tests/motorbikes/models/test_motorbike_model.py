from django.test import TestCase

from finalProject.motorbike.models import Motorbike
from finalProject.user_profile.models import CollectionUser


class MotorbikeTests(TestCase):
    VALID_MOTORBIKE_DATA = {
        'bike_type': 'Scooter',
        'model': 'BMW',
        'year': '2000',
        'engine_size': '250',
        'fuel_capacity': '35',
        'fuel_type': 'А95Н',
        'top_speed': '180',
        'emission_standard': 'Euro V',
        'image': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/'
                 'car-reviews/first-drives/legacy/10-porsche-718-cayman-gt4-rs-top-10.jpg?itok=BacF-43A',
        'price': '1200',
    }
    VALID_USER_DATA = {
        'username': 'testusername',
        'email': 'test3@test3.com',
        'phone_number': '0896207842',
        'password': 'Yoan1234',

    }

    def test_create__when_valid__expect_to_be_created(self):
        user = CollectionUser.objects.create(**self.VALID_USER_DATA)
        bike = Motorbike.objects.create(**self.VALID_MOTORBIKE_DATA, user=user)
        bike.full_clean()
        bike.save()

        self.assertIsNotNone(bike.pk)