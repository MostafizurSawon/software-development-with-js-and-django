from django.shortcuts import render

# Create your views here.

def about(request):
  print(request.GET)
  return render(request, 'about.html')