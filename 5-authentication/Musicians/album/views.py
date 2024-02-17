from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import Add_Album, Add_Musician, Edit_Musician, Edit_Album

# Create your views here.

from . models import Album, Musician
def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {"albums":albums})

def addMusician(request):
    if request.method == "POST":
        form = Add_Musician(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = Add_Musician()
    return render(request, 'add-musicians.html', {"form":form})


def addAlbum(request):
    if request.method == "POST":
        form = Add_Album(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = Add_Album()
    return render(request, 'add-album.html',{"form":form})



def editMusician(request, id):
    musician = Musician.objects.get(id = id)
    if request.method == "POST":
        form = Edit_Musician(request.POST, instance= musician)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = Edit_Musician(instance=musician)
        return render(request, 'add-musician.html', {"form": form})



def deleteMusician(request, id):
    Musician.objects.get(id = id).delete()
    return redirect("homepage")
 
def editAlbum(request, id):
    album = Album.objects.get(id = id)
    if request.method == "POST":
        form = Edit_Album(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = Edit_Album(instance=album)
    return render(request, 'add-album.html',{"form":form})