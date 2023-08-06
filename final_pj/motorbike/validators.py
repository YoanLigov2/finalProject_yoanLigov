from django.core.validators import ValidationError


def check_year(value):
    if not (1980 <= value <= 2023):
        raise ValidationError("Year must be between 1980 and 2023!")


def engine_size_validator(value):
    if value < 49:
        raise ValidationError('Engine size can not be lesser than 49!')


def fuel_capacity_validator(value):
    if value < 6:
        raise ValidationError('Fuel Capacity can not be lesser than 6 liters!')


def top_speed_validator(value):
    if value < 50:
        raise ValidationError('Top speed must be greater or equal to 50!')


def price_validator(value):
    if value < 100:
        raise ValidationError('Please select price greater than 100!')