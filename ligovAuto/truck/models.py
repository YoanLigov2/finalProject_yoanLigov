from django.contrib.auth import get_user_model
from django.db import models
from .validators import check_year, check_mass, check_height, check_price, check_engine


user_model = get_user_model()


class Truck(models.Model):

    image = models.ImageField(upload_to='images/trucks')

    model = models.CharField(
        max_length=10,
        choices=(
            ("Man", "Man"),
            ("Volvo", "Volvo"),
            ("Mercedes", "Mercedes"),
            ("Scania", "Scania"),
            ("Other", "Other"),
        ),
    )

    year = models.IntegerField(
        validators=[check_year],
    )

    truck_mass = models.FloatField(
        validators=[check_mass]
    )

    truck_height = models.FloatField(
        validators=[check_height]
    )

    engine_power = models.FloatField(
        validators=[check_engine]
    )

    price = models.FloatField(
        validators=[check_price],
    )

    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE)

    very_short_description = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.model}#{self.pk}'