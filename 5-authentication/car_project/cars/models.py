from django.db import models
from car_brand.models import car_brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    car_brand = models.ForeignKey(car_brand,on_delete=models.CASCADE) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/media/uploads/', blank = True, null = True)
    cart = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'cars')
    
    def __str__(self):
        return self.name 
    
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"


    