from django.contrib.auth import get_user_model
from django.db import models
from .validators import check_year, engine_size_validator, fuel_capacity_validator, top_speed_validator, price_validator


user_model = get_user_model()


class Motorbike(models.Model):

    bike_type = models.CharField(
        max_length=10,
        choices=(
            ("Scooter", "Scooter"),
            ("Chopper", "Chopper"),
            ("Sportbike", "Sportbike"),
            ("Off-Road", "Off-Road"),
            ("Other", "Other"),
        ),
    )

    model = models.CharField(
        max_length=30
    )

    year = models.IntegerField(
        validators=[check_year]
    )

    engine_size = models.IntegerField(
        validators=[engine_size_validator]
    )

    fuel_capacity = models.IntegerField(
        validators=[fuel_capacity_validator]
    )

    fuel_type = models.CharField(
        max_length=11,
        choices=(
            ("Diesel", "Diesel"),
            ("А95Н", "А95Н"),
            ("LPG", "LPG"),
            ("Electricity", "Electricity"),
            ("Other", "Other"),
        ),
    )

    top_speed = models.IntegerField(
        validators=[top_speed_validator]
    )

    emission_standard = models.CharField(
        max_length=8,
        choices=(
            ("Euro I", "Euro I"),
            ("Euro II", "Euro II"),
            ("Euro III", "Euro III"),
            ("Euro IV", "Euro IV"),
            ("Euro V", "Euro V"),
            ("Euro V+", "Euro V+"),
        ),
    )

    price = models.FloatField(
        validators=[price_validator]
    )

    image = models.URLField()

    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE)

    short_description = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.model}#{self.pk}'