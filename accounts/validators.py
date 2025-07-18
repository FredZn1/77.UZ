import re
from rest_framework.exceptions import ValidationError


def validate_phone_number(value):
    if not re.fullmatch(r'^\+998\d{9}$', value):
        raise ValidationError("Telefon raqami +998XXXXXXXXX formatida bo'lishi kerak.")
    return value
