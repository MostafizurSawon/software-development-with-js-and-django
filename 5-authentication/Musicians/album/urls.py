from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'homepage'),
    path("addMusician/", views.addMusician, name = 'addMusician'),
    path('addAlbum/', views.addAlbum, name = 'addAlbum'),
    path("EditMusician/<int:id>/", views.editMusician, name = 'editMusician'),
    path("deleteMusician/<int:id>/", views.deleteMusician, name = 'deleteMusician'),
    path("editAlbum/<int:id>/", views.editAlbum, name = 'editAlbum'),
    
]