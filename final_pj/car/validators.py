from django.core.validators import ValidationError


def check_year(value):
    if not (1980 <= value <= 2023):
        raise ValidationError("Year must be between 1980 and 2023!")


def horse_power_validator(value):
    if value < 100:
        raise ValidationError("Please select horse powers value greater or equal than 100!")


def price_validator(value):
    if value < 200:
        raise ValidationError('The price can not be lesser than 200!')


def top_speed_validator(value):
    if value < 200:
        raise ValidationError('Top speed must be greater or equal to 200!')