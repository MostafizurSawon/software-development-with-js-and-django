from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add-car-brand/', views.add_car_model, name='add_brand')
]