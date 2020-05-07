from django import forms
from django.contrib.auth.models import User
from .models import Expense

class ExpenseEntryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title', 'class':'form-control'}))
    description = forms.Textarea(widget=forms.TextInput(attrs={'placeholder': 'Desfription', 'class':'form-control'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Amount', 'class':'form-control'}))
    
    class Meta:
        model = Expense
        fields = ('title', 'description', 'amount')
