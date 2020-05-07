from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "drugs"

urlpatterns = [    
    path('add/', views.add_drug, name = "add_drug"),
    path('view/', views.view_all, name = "view_drugs"),
    path('view/<int:pk>', views.view_drug, name = "view_drug"),

    '''
    Layer on we will have paths for
    edit
    delete
    ...

    '''
    
    
]
