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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control-file',
        })
        self.fields['biography'].widget.attrs.update({
            'class': 'form-control',
        })
