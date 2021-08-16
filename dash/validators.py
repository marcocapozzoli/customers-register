from django.core.exceptions import ValidationError
import re

def validate_phone(value):
    
    # 11 digits
    if len(str(value)) > 11:
        raise ValidationError(
            'Informe um número válido.',
            params={'value': value},
        )
    # # DDD
    # if len(str(value)) == 9 and :
    #     raise ValidationError(
    #         'Informe um número válido.',
    #         params={'value': value},
    #     )
    