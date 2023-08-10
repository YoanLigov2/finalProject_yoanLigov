from django.test import TestCase

from ligovAuto.yacht.models import Yacht
from ligovAuto.user_profile.models import CollectionUser


class YachtModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for ForeignKey reference
        cls.user = CollectionUser.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='1234567890',
            password='testpassword'
        )

        # Create a yacht instance
        cls.yacht = Yacht.objects.create(
            image='path/to/image.jpg',
            style='Cruiser',
            classification='Class A',
            engines='Full-displacement hull',
            yacht_length=20.5,
            price=1000000.0,
            user=cls.user,
            very_short_description='Test yacht description'
        )

    def test_model_fields(self):
        # Check if model fields are correctly defined
        yacht = self.yacht
        self.assertEqual(yacht.image, 'path/to/image.jpg')
        self.assertEqual(yacht.style, 'Cruiser')
        self.assertEqual(yacht.classification, 'Class A')
        self.assertEqual(yacht.engines, 'Full-displacement hull')
        self.assertEqual(yacht.yacht_length, 20.5)
        self.assertEqual(yacht.price, 1000000.0)
        self.assertEqual(yacht.user, self.user)
        self.assertEqual(yacht.very_short_description, 'Test yacht description')

    def test_str_method(self):
        # Check if __str__() method returns the expected string representation
        yacht = self.yacht
        expected_str = f'{yacht.style}#{yacht.pk}'
        self.assertEqual(str(yacht), expected_str)
