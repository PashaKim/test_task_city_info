from django.core.exceptions import ValidationError


def validate_decimals_3(value):
    try:
        return round(float(value), 3)
    except:
        raise ValidationError(
            '%(value)s is not an integer or a float  number',
            params={'value': value},
        )
