from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import only_alphabetical_letters


class CollectionUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_alphabetical_letters
        )
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_alphabetical_letters
        )
    )
    gender = models.CharField(
        max_length=len("Do not show"),
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Do not show', 'Do not show')
        )
    )
    profile_picture = models.URLField()

    def get_user_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.last_name or self.first_name:
            return self.first_name or self.last_name
        else:
            return self.username
