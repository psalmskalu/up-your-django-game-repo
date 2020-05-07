from django.shortcuts import render
from .forms import SaleEntryForm
from .models import Sale

# Create your views here.

def add_Sale(request):
    user = request.user

    if request.method == 'POST':

        form = SaleEntryForm(request.POST)
        if form.is_valid:
            sale = form.save(commit=False)
            sale.set_user(user)
            sale.save()

            return render(request, "sales/add_sale_successful.html", {})

        else:

            return render(request, "sales/add_sale_failed.html", {})
            
    else:

        form = SaleEntryForm()
        context = {
            'user':user,
           'form':form
        }
        return render(request, "sales/add_sale.html", context)



def view_all(request):
    pass

def view_Sale(request):
    pass