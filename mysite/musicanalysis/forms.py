from django import forms
from .models import PlaylistIdModel


class PlaylistIdForm(forms.ModelForm):
    class Meta:
        model = PlaylistIdModel
        fields = ("playlist_id",)
