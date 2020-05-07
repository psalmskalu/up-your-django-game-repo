from django.shortcuts import render
from .forms import ExpenseEntryForm
from .models import Expense

# Create your views here.

def add_expense(request):

    user = request.user

    if request.method == 'POST':

        form = ExpenseEntryForm(request.POST)
        if form.is_valid:
            expense = form.save(commit=False)
            expense.set_user(user)
            expense.save()

            return render(request, "expenses/add_expense_successful.html", {})

        else:

            return render(request, "expenses/add_expense_failed.html", {})
            
    else:

        form = ExpenseEntryForm()
        context = {
            'user':user,
           'form':form
        }
        return render(request, "drugs/add_drug.html", context)


def view_all(request):
    pass

def view_expense(request):
    pass