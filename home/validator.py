from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from mainApp.models import User

def email_used_validator(email):
    not_unique = User.objects.filter(email__iexact=email).exists()
    if not_unique:
        raise ValidationError(
            _('%(email)s is already used.'),
            params={'email': email},
        )