from django import forms
from .models import PlaylistUrlModel


class PlaylistIdForm(forms.ModelForm):
    class Meta:
        model = PlaylistUrlModel
        fields = ("playlist_url",)

    def clean_url(self):
        value = self.cleaned_data["playlist_url"]
        check_url = "https://open.spotify.com/playlist/42vVvTztB8SlSM4Lnk5IZQ"
        if value not in check_url:
            raise forms.ValidationError(
                "URLを正しく入力してください。"
            )
        return value