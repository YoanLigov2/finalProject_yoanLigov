from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import only_alphabetical_letters, phone_number_validator


class CollectionUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='images/profile_pictures',
        blank=True,
        null=True,
    )

    email = models.EmailField(unique=True)

    phone_number = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10),
            phone_number_validator,
        ],
        unique=True
    )

    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_alphabetical_letters
        ),
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_alphabetical_letters
        ),
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=len("Do not show"),
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Do not show', 'Do not show')
        ),
        blank=True,
        null=True
    )

    def get_user_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.last_name or self.first_name:
            return self.first_name or self.last_name
        else:
            return self.username

    def __str__(self):
        return f'{self.username}'
