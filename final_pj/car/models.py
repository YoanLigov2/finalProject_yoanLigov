from django.contrib.auth import get_user_model
from django.db import models
from .validators import check_year, horse_power_validator, price_validator, top_speed_validator


user_model = get_user_model()


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
    )

    model = models.CharField(
        max_length=30
    )

    year = models.IntegerField(
        validators=[check_year]
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

    horse_power = models.IntegerField(
        validators=[horse_power_validator]
    )

    image = models.URLField()

    price = models.FloatField(
        validators=[price_validator]
    )

    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE)

    short_description = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.model}#{self.pk}'
