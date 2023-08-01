# login_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login_ok/', views.login_ok, name='login_ok'),
    path('login/', views.login_view, name='login'),
    # Agrega aquí otras URL de tu aplicación Django
]
