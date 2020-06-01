from django import forms

from .models import Commentarie


class CommentarieForm(forms.ModelForm):
    class Meta:
        model = Commentarie
        fields = [
            'title', 'description', 'image', 'slug'
        ]
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'image': 'Imagen',
        }
