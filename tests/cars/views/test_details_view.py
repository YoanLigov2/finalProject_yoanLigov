from django.test import TestCase, Client
from django.urls import reverse
from ligovAuto.car.models import Car
from ligovAuto.user_profile.models import CollectionUser


class CarDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user
        self.user = CollectionUser.objects.create_user(
            username='test_user',
            email='test@example.com',
            phone_number='1234567890',
            password='test_password'
        )
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
        self.url = reverse('car-details', args=[self.car.pk])

    def test_car_details_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car/car-details.html')
        self.assertIn('car', response.context)
        self.assertIn('owner', response.context)
        self.assertEqual(response.context['car'], self.car)
        self.assertEqual(response.context['owner'], self.user)

    def test_invalid_car_details_view(self):
        invalid_url = reverse('car-details', args=[9999])
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 404)
