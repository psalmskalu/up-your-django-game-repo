from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "accounts"

urlpatterns = [    
    path('login/', views.user_login, name = "login"),
    path('signup/', views.user_signup, name = "signup"),
    path('logout/', views.user_signout, name = "signout"),
    path('dashboard/', views.user_dashboard, name = "dashboard")
    
]
