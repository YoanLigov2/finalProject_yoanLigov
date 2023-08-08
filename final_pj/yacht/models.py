from django.contrib.auth import get_user_model
from django.db import models
from .validators import check_length, check_price


user_model = get_user_model()


class Yacht(models.Model):

    image = models.ImageField(upload_to='images/yachts')

    style = models.CharField(
        max_length=16,
        choices=(
            ("Cruiser", "Cruiser"),
            ("Sports cruiser", "Sports cruiser"),
            ("Sports fisherman", "Sports fisherman"),
            ("Expedition", "Expedition"),
            ("Lobster", "Lobster"),
            ("Trawler", "Trawler"),
            ("Other", "Other"),
        )
    )

    classification = models.CharField(
        max_length=7,
        choices=(
            ("Class A", "Class A"),
            ("Class 1", "Class 1"),
            ("Class 2", "Class 2"),
            ("Class 3", "Class 3"),
        )
    )

    engines = models.CharField(
        max_length=22,
        choices=(
            ("Full-displacement hull", "Full-displacement hull"),
            ("Semi-displacement hull", "Semi-displacement hull"),
            ("Planing hull", "Planing hull"),
        )
    )

    yacht_length = models.FloatField(
        validators=[check_length]
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
        return f'{self.style}#{self.pk}'
