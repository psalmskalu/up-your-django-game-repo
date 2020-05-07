from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "expenses"

urlpatterns = [    
    path('add/', views.add_expense, name = "add_expense"),
    path('view/', views.view_all, name = "view_expenses"),
    path('view/<int:pk>', views.view_expense, name = "view_expense"),

    '''
    Layer on we will have paths for
    edit
    delete
    ...

    '''
    
    
]
