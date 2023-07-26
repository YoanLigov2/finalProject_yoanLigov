from django.test import TestCase

from finalProject.yacht.models import Yacht
from finalProject.user_profile.models import CollectionUser


class YachtTests(TestCase):
    VALID_YACHT_DATA = {
        'style': 'Cruiser',
        'classification': 'Class A',
        'engines': 'Full-displacement hull',
        'yacht_length': '16',
        'image_url': 'https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/'
                 'car-reviews/first-drives/legacy/10-porsche-718-cayman-gt4-rs-top-10.jpg?itok=BacF-43A',
        'price': '1200000',
    }
    VALID_USER_DATA = {
        'username': 'testusername',
        'email': 'test3@test3.com',
        'phone_number': '0896207842',
        'password': 'Yoan1234',

    }

    def test_create__when_valid__expect_to_be_created(self):
        user = CollectionUser.objects.create(**self.VALID_USER_DATA)
        yacht = Yacht.objects.create(**self.VALID_YACHT_DATA, user=user)
        yacht.full_clean()
        yacht.save()

        self.assertIsNotNone(yacht.pk)