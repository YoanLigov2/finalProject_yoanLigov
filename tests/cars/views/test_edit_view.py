from django.test import TestCase, Client
from django.urls import reverse
from ligovAuto.car.models import Car
from ligovAuto.user_profile.models import CollectionUser


class CarEditViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user
        self.user = CollectionUser.objects.create_user(
            username='test_user',
            email='test@example.com',
            phone_number='1234567890',
            password='test_password'
        )
        self.client.login(username='test_user', password='test_password')

        # Create a test car
        self.car = Car.objects.create(
            car_type='Sports Car',
            model='Test Model',
            year=2022,
            fuel_type='Diesel',
            top_speed=200,
            emission_standard='Euro V',
            horse_power=300,
            image='path/to/image.png',
            price=50000.0,
            user=self.user,
            short_description='Test Description'
        )
        self.url = reverse('car-edit', args=[self.car.pk])

    def test_car_edit_view(self):
        # Updated car data
        updated_data = {
            'car_type': 'Pickup',
            'model': 'Updated Model',
            'year': 2023,
            'fuel_type': 'А95Н',
            'top_speed': 220,
            'emission_standard': 'Euro V+',
            'horse_power': 350,
            'image': 'path/to/image2.png',
            'price': 60000.0,
            'short_description': 'Updated Description'
        }

        response = self.client.post(self.url, data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.car.car_type, updated_data['car_type'])
        expected_url = reverse('car-details', kwargs={'pk': self.car.pk})
        self.assertRedirects(response, expected_url)
