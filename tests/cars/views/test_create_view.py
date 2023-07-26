from django.test import TestCase
from django.urls import reverse

from finalProject.car.models import Car
from finalProject.user_profile.models import CollectionUser


class CreateViewTests(TestCase):
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
    VALID_USER_DATA = {
        'username': 'testusername',
        'email': 'test3@test3.com',
        'phone_number': '0896207842',
        'password': 'Yoan1234',

    }

    def test_create_post__when_valid__expect_to_be_created(self):
        # Act
        response = self.client.post(
            reverse('car-create'),
            data={
                **self.VALID_CAR_DATA,
                **self.VALID_USER_DATA,
            }
        )

        # Assert
        user = CollectionUser.objects.create(
            **self.VALID_USER_DATA,
        )
        car = Car.objects.create(
            **self.VALID_CAR_DATA,
            user=user,
        )

        self.assertEqual(302, response.status_code)
        self.assertIsNotNone(user)
        self.assertIsNotNone(car)