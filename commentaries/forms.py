from django.forms import ModelForm

from .models import Commentarie


class CommentarieForm(ModelForm):
    class Meta:
        model = Commentarie
        fields = [
            'title', 'description', 'image'
        ]
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'image': 'Imagen',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })
