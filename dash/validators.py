from django.core.exceptions import ValidationError
import re

def validate_phone(value):
    resposta = re.findall('[0-9]{2} [0-9]{5}-[0-9]{4}', value)
    if len(resposta) == 0:
        raise ValidationError(
            'Informe um número no seguinte padrão: 99 99999-9999',
            params={'value': value},
        )