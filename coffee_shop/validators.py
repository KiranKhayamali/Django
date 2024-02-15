from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_zipcode(value):
    if len(value) != 4:
        raise ValidationError(_("Zipcode needs to be of length 4: %(value)s"), 
                                code='invalid',
                                params={'value': value},
                                )