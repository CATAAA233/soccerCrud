from django import forms


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


class playersRegisterForm(forms.Form):
    name = forms.CharField(max_length=30)
    team = forms.CharField(max_length=30,)
    age = forms.CharField( max_length=3)
    position = forms.CharField(max_length=20)
    number = forms.CharField(max_length=2)
    image = forms.ImageField()


    def __str__(self):
        return self.name