from django import forms

class SearchForm(forms.Form):
    item = forms.CharField(required=True, max_length=100)

