from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "sales"

urlpatterns = [    
    path('add/', views.add_sale, name = "add_sale"),
    path('view/', views.view_all, name = "view_sales"),
    path('view/<int:pk>', views.view_sale, name = "view_sale"),

    '''
    Layer on we will have paths for
    edit
    delete
    ...

    '''
    
    
]
