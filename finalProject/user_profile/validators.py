from django.core.validators import ValidationError


def only_alphabetical_letters(value):
    if not value.isalpha():
        raise ValidationError("Must contain only alphabetical letters!!!")