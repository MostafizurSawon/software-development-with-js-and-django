from django.shortcuts import render
from album.models import Album

def home(request):
    data = Task.objects.all()
    return render(request, 'home.html', {'data' : data})

def main(request):
    data = Task.objects.all()
    return render(request, 'main.html', {'data' : data})