"""
URL configuration for static_rev_11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name = 'app_home'),
    path('table/', views.table, name = 'table'),
    path('form/', views.form, name = 'form'),
    path('django-form/', views.djangoForm, name = 'django_form'),
    # path('student-form/', views.StudentForm, name = 'student_form'),
    path('student-form/', views.PasswordValidation, name = 'student_form'),
    path('about/', views.about, name = 'about'),
    path('student/', views.student_home, name = 'sthome'),
    path('stmodel/', views.stmodel, name = 'stmodelform'),
    path('delete/<int:roll>', views.delete_student, name="delete_student"),
]
