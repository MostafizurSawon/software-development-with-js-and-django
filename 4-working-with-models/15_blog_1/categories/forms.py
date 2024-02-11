from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = '__all__'

        # widgets = {
        #     "title" : TextInput(attrs={"class" : "title"}),
        # }
        labels = {
            "name": ("Category Name: "),
        }