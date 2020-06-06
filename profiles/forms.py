from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'avatar', 'biography'
        ]
        labels = {
            'avatar': 'Imagen del perfil',
            'biography': 'Biografia',
        }
