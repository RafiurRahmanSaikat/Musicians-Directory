from django import forms
from .models import AlbumModel


class AlbumForm(forms.ModelForm):

    class Meta:
        model = AlbumModel
        fields = "__all__"
        widgets = {
            "musicians": forms.CheckboxSelectMultiple(),
            "rating": forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
        }
