from django.core.validators import ValidationError


def only_alphabetical_letters(value):
    if not value.isalpha():
        raise ValidationError("Must contain only alphabetical letters!!!")


def phone_number_validator(value):
    if not value.isdigit() or not value.startswith('0'):
        raise ValidationError('Please type valid phone number !')
