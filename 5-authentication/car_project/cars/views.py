from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from cars.models import Car
from . import forms
from . import models
# Create your views here.

# Add Car using class Based view
@method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_new_car')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class EditCarView(UpdateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class DeleteCarView(DeleteView):
    model = models.Car
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form

        return context
    

def carBuy(request, id):
    if not request.user.is_authenticated:
        return redirect("user_login") 
    car = Car.objects.get(id = id)
    if car.quantity > 0:
        car.quantity -= 1
    car.cart = request.user 
    car.save()
    return redirect("profile")
