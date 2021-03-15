from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneValidator(RegexValidator):
    """Phone number validation.

    The phone number can only contain numbers.
    Number length is from 12 to 15 digits.
    """
    regex = r'^\d{12,15}$'
    message = "Не правильный формат номера телефона."
