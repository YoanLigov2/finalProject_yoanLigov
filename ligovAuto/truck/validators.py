from django.core.validators import ValidationError


def check_year(value):
    if not (1980 <= value <= 2023):
        raise ValidationError("Year must be between 1980 and 2023!")


def check_mass(value):
    if value < 11:
        raise ValidationError("Truck mass can not be lesser than 11 tons!")


def check_height(value):
    if not 3 <= value <= 6:
        raise ValidationError("Please select real height!")


def check_price(value):
    if value < 100000:
        raise ValidationError("Please select price equal or greater than 100_000!")


def check_engine(value):
    if value < 400:
        raise ValidationError("Engine power must be higher or equal to 400hp!")