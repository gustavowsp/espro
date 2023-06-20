from django.urls import path
from . import views

urlpatterns = [
    path('', views.vagas, name='listador-de-vagas')
]