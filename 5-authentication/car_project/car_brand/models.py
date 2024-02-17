from django.db import models

# Create your models here.
class car_brand(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50,unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name