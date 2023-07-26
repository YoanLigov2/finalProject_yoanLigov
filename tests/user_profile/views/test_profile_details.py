from django.test import TestCase, Client
from django.urls import reverse
from finalProject.user_profile.models import CollectionUser


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
        self.url = reverse('profile-details', args=[self.user.pk])

    def test_profile_details_view(self):
        response = self.client.get(self.url)
        # self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-details.html')
        # Check if the car object in context matches the created car
        self.assertEqual(response.context['object'], self.user)
