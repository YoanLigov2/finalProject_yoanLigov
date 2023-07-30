from django.test import TestCase
from finalProject.user_profile.models import CollectionUser


class UserRegistrationViewTest(TestCase):

    def test_user_model_valid_data(self):
        user = CollectionUser(
            username='testuser',
            email='test@example.com',
            phone_number='0234567890',
            password='testpassword123',
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user)
