from django.urls import path
from . views import add_post,delete_post,edit_post

urlpatterns = [
    path('add-post/', add_post, name='add_post'),
    path('edit/<int:id>', edit_post, name='edit_post'),
    path('delete/<int:id>', delete_post, name='delete_post'),
]
