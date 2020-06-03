from django import forms

from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=25,
        required=True,
        label='Nombre de Usuario',
        widget=forms.TextInput(
            attrs={
                'data-role':'input'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label='Correo Electronico',
        widget=forms.EmailInput(
            attrs={
                'data-role':'input'
            }
        )
    )
    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'data-role':'input'
            }
        )
    )
    password2 = forms.CharField(
        required=True,
        label='Repita la contraseña',
        widget=forms.PasswordInput(
            attrs={
                'data-role':'input'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya esta en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo de usuario ya esta en uso')
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )
