from django import forms
from . models import Musician, Album

class Add_Musician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class Edit_Musician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class Add_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class Edit_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
