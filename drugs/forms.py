from django import forms
from django.contrib.auth.models import User
from .models import Drug

class DrugEntryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Quantity', 'class':'form-control'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Price', 'class':'form-control'}))
    mf_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Manufacturing Date', 'class':'form-control'}))
    exp_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Expiry Date', 'class':'form-control'}))

    class Meta:
        model = Drug
        fields = ('name', 'quantity', 'price', 'mf_date', 'exp_date')
