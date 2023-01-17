from django import forms


class SearchPassForm(forms.Form):
    search_pass = forms.URLField(label='url', min_length=1,
                                 widget=forms.Textarea(attrs={'placeholder': 'ここにURLを入力してください'}))
