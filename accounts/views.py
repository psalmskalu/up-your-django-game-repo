from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm

# Create your views here.
def user_login(request):
    form = LoginForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def user_signup(request):
    form = RegistrationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)
