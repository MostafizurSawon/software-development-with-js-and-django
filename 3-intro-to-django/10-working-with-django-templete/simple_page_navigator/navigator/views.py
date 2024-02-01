from django.shortcuts import render
import datetime

# Create your views here.

def about(request):
    person = {'name':'Md Mostafizur Rahman', 'age': 28, 'date':datetime.datetime.now(), 'district': 'Natore', 'rolls':[4,3,2], 'courses':[
        {
            'id':1,
            'name': 'Python',
            'des': 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.',
            'fee': 3000

        },
        {
            'id':2,
            'name': 'OOP with Python',
            'des': 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.',
            'fee': 4000

        },
        {
            'id':3,
            'name': 'Django with Python',
            'des': 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.',
            'fee': 8000

        }

    ]}
    return render(request, 'navigator/about.html', person)

def contact(request):
    return render(request, 'navigator/contact.html')