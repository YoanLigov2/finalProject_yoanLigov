from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class LoginUserViewTests(TestCase):
    def test_login_user(self):
        user_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        user_create_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone_number': '0234567890',
            'password': 'testpassword123',
        }
        user = UserModel.objects.create_user(**user_create_data)

        response = self.client.post(
            reverse('login'),
            data={
                **user_data,
            }
        )
        self.assertEqual(302, response.status_code)
        self.assertIsNotNone(user)

