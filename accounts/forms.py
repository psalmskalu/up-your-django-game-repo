from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Firstname', 'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Surname', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def validate_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")

        return cd["password2"]
