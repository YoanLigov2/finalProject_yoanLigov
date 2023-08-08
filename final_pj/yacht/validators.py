from django.core.validators import ValidationError


def check_length(value):
    if value < 10:
        raise ValidationError('Yacht length can not be lesser than 10 meters!')


def check_price(value):
    if value < 1_000_000:
        raise ValidationError('Yacht price can not be lesser than 1 mill !')