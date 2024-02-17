from django.shortcuts import render
from cars.models import Car
from car_brand.models import car_brand

def home(request, brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = car_brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(car_brand=brand)
    brands = car_brand.objects.all()
    return render(request, 'home.html', {'data' : data, 'car_brand' : brands})
