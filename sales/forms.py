from django import forms
from django.contrib.auth.models import User
from .models import Sale

class SaleEntryForm(forms.ModelForm):

    drug = forms.Field(widget=forms.TextInput(attrs={'placeholder':'Title', 'class':'form-control'}))
    customer = forms.Textarea(widget=forms.TextInput(attrs={'placeholder': 'Desfription', 'class':'form-control'}))    
    quantity = forms.Textarea(widget=forms.TextInput(attrs={'placeholder': 'Desfription', 'class':'form-control'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Amount', 'class':'form-control'}))
    date_of_sale = forms.Textarea(widget=forms.TextInput(attrs={'placeholder': 'Desfription', 'class':'form-control'}))
    
    class Meta:
        model = Sale
        fields = ('title', 'description', 'amount')
