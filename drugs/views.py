from django.shortcuts import render
from .forms import DrugEntryForm
from .models import Drug

# Create your views here.

def add_drug(request):
    user = request.user

    if request.method == 'POST':

        form = DrugEntryForm(request.POST)
        if form.is_valid:
            drug = form.save(commit=False)
            drug.set_user(user)
            drug.save()

            return render(request, "drugs/add_drug_successful.html", {})

        else:

            return render(request, "drugs/add_drug_failed.html", {})
            
    else:

        form = DrugEntryForm()
        context = {
            'user':user,
           'form':form
        }
        return render(request, "drugs/add_drug.html", context)



def view_all(request):
    pass

def view_drug(request):
    pass