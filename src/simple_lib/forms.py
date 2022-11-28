from django import forms

class ReaderNumberForm(forms.Form):
    number = forms.IntegerField(label='numer karty bibliotecznej')


class BookNumberForm(forms.Form):
    number = forms.IntegerField(label='numer katalogowy książki')
    
