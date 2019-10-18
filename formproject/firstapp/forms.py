from django import forms

class FormName(forms.Form):
    pass
    
class Form1(forms.Form):
    text=forms.CharField(label='insect')

class FormEmpty(forms.Form):
    pass
