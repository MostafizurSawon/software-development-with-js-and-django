from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name = 'home'),
    path('about/', views.index, name = 'about'),
]