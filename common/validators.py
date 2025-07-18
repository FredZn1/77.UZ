from rest_framework.exceptions import ValidationError
import re


def validate_slug(value):
    if not re.match(r"^[a-z0-9-]+$", value):
        raise ValidationError("Slug faqat kichik harflar, raqamlar va `-` belgidan iborat bo'lishi kerak.")
    return value
