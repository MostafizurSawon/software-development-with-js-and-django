from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

# Create your views here.
def index(request):
    d = {'author' : 'Rahim"s Court', 'age' : 5, 'lst' : ['python','is','the','best'], 'birthday' : datetime.datetime.now(), 'val' : '' ,'courses' : [
        
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000 
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000 
        },
        {
            'id' : 4,
            'name' : 'C',
            'fee' : 1000 
        },
    ]}
    return render(request, 'my_app/index.html', d)