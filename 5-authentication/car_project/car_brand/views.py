from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_car_model(request):
    if request.method == 'POST': 
        add_car_form = forms.carBrandForm(request.POST)
        if add_car_form.is_valid(): 
            add_car_form.save() 
            return redirect('add_brand')
    
    else: 
        add_car_form = forms.carBrandForm()
    return render(request, 'add_model.html', {'form' : add_car_form})