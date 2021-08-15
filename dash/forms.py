from dash.models import Person
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .validators import *


class PersonForm(forms.Form):
    
    LABEL = (
        ('Frio','Frio'),
        ('Morno','Morno'),
        ('Quente','Quente'),
    )
    
    first_name = forms.CharField(
        label='', 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome'}),
        max_length=15
    )
    last_name = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
        max_length=15
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    )
    birthday = forms.DateField(
        label='',
        #widget=forms.DateInput(attrs={'type':'date'})
        widget=AdminDateWidget(attrs={'placeholder': 'Aniversário'})
    ) 
    phone = forms.CharField(
        label='',
        max_length=13,
        validators=[validate_phone],
        widget=forms.TextInput(attrs={'placeholder': 'Telefone: 99 99999-9999'})
    )
    company = forms.CharField(
        label='',
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Empresa'})
    )
    label = forms.ChoiceField(
        label='',
        choices=LABEL,
    )

class PersonDetailForm(PersonForm):
    note = forms.CharField(max_length=60)