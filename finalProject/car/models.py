from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .validators import check_year


class Car(models.Model):
    car_type = models.CharField(
        max_length=10,
        choices=(
            ("Sports Car", "Sports Car"),
            ("Pickup", "Pickup"),
            ("Crossover", "Crossover"),
            ("Minibus", "Minibus"),
            ("Other", "Other"),
        ),
        blank=False,
        null=False
    )

    model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        blank=False,
        null=False
    )

    year = models.IntegerField(
        validators=[check_year],
        blank=False,
        null=False
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )

    price = models.FloatField(
        validators=[MinValueValidator(1)],
        blank=False,
        null=False
    )