from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "customers"

urlpatterns = [    
    path('add/', views.add_customer, name = "add_customer"),
    path('view/', views.view_all, name = "view_customers"),
    path('view/<int:pk>', views.view_customer, name = "view_customer"),

    '''
    Layer on we will have paths for
    edit
    delete
    ...

    '''
    
    
]
