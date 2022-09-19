from django import forms
from .models import stadiumsModel


class stadiumsRegisterForm(forms.Form):
    name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=50)
    capacity = forms.CharField(max_length=10)
    image = forms.ImageField()

class teamsRegisterForm(forms.Form):
    name = forms.CharField( max_length=30)
    location = forms.CharField(max_length=50)
    stadium = forms.CharField(max_length=30)
    nickname = forms.CharField( max_length=15)
    image = forms.ImageField()
