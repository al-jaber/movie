from django import forms

class MovieForm(forms.Form):
    name = forms.CharField(max_length=65)
