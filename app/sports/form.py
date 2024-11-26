from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()

class PrimeNumbersForm(forms.Form):
    start = forms.IntegerField()
    stop = forms.IntegerField()