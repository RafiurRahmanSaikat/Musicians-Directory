from django import forms
from .models import MusicianModel


class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = "__all__"
