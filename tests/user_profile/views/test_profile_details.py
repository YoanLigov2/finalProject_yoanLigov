from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


UserModel = get_user_model()


class ProfileDetailsViewTest(TestCase):
    def test_profile_details_view(self):
        user_create_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone_number': '0234567890',
            'password': 'testpassword123',
        }
        user = UserModel.objects.create_user(**user_create_data)
        url = reverse('profile-details', args=[user.pk])
        response = self.client.get(url)
        # self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-details.html')

        self.assertEqual(response.context['object'], self.user)
