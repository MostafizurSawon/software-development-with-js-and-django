from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:id>', views.edit_task, name='edit_task'),
    path('delete-task/<int:id>', views.delete_task, name='delete_task'),
]