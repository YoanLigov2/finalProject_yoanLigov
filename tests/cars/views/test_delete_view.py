from django.test import TestCase, Client
from django.urls import reverse
from ligovAuto.car.models import Car
from ligovAuto.user_profile.models import CollectionUser


class CarDeleteViewTest(TestCase):
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
        self.url = reverse('car-delete', args=[self.car.pk])

    def test_car_delete_view(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Car.objects.filter(pk=self.car.pk).exists())
        expected_url = reverse('catalogue')
        self.assertRedirects(response, expected_url)
