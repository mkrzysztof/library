from django import forms

class ReaderNumberForm(forms.Form):
    number = forms.IntegerField(label='numer karty bibliotecznej')
