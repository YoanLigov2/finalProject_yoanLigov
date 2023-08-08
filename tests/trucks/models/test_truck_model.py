from django.test import TestCase

from finalProject.truck.models import Truck
from finalProject.user_profile.models import CollectionUser


class TruckTests(TestCase):
    VALID_TRUCK_DATA = {
        'model': 'Man',
        'year': '2000',
        'truck_mass': '15',
        'truck_height': '4.5',
        'engine_power': '600',
        'image_url': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/'
                 'car-reviews/first-drives/legacy/10-porsche-718-cayman-gt4-rs-top-10.jpg?itok=BacF-43A',
        'price': '120000',
    }
    VALID_USER_DATA = {
        'username': 'testusername',
        'email': 'test3@test3.com',
        'phone_number': '0896207842',
        'password': 'Yoan1234',

    }

    def test_create__when_valid__expect_to_be_created(self):
        user = CollectionUser.objects.create(**self.VALID_USER_DATA)
        truck = Truck.objects.create(**self.VALID_TRUCK_DATA, user=user)
        truck.full_clean()
        truck.save()

        self.assertIsNotNone(truck.pk)