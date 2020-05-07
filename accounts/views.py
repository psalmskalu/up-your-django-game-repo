from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("Login successful")

            else:
                
                form = LoginForm()
                context = {
                    'form': form,
                    'message':'Incorrect login'
                }
                return render(request, 'accounts/login.html', context)

        else:
            form = LoginForm()
            context = {
                    'form': form,
                    'message':'Form failed to process'
                }
            return render(request, 'accounts/login.html', context)

    else:
        
        form = LoginForm()
        context = {
                    'form': form,
                    
                }
        return render(request, 'accounts/login.html', context)



def user_signup(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid:

            #create new user
            user = form.save(commit=False)

            #assign password to user
            user.set_password(form.cleaned_data["password"])

            #save new user
            user.save()

            return HttpResponse("New User created successfully!")

        else:

            context = {
                'form':form,
                'message':'oops! Something went wrong!'
            }
            return render(request, 'accounts/signup.html', context)

    else:
        form = RegistrationForm()
        context = {
                'form':form,
                
            }

        return render(request, 'accounts/signup.html', context)

        
    
    
    form = RegistrationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)
