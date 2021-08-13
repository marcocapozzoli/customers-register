from django.contrib.auth import forms, password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms

from users.models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# Sign Up Form
class SignupForm(CustomUserCreationForm):
    
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Escolha um nome de usuário'
        }),
        max_length=20,
        error_messages={
            'unique': 'Já existe um usuário cadastrado com esse nome.'
        }
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})    
    )
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'}),
        strip=False,
    )
    
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']

# Login Form
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label = '',
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'placeholder' : 'Usuário'
        }))
    password = forms.CharField(
        label = '',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),
    )

    
# ResetPassword Form
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'placeholder': 'Insira o seu endereço de email'})
    )
    
# ResetPasswordConfirm Form
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder' : 'Nova Senha'}),
        strip=False
    )
    new_password2 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder' : 'Confirme a Senha'}),
    )
