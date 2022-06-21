from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Registration(models.Model):
    gender_choice=(
    ('Male','Male'),
    ('Female','Female'),
    )
    name=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField(max_length=254)
    contact_number=models.CharField(max_length=20)
    gender=models.CharField(max_length=100,choices=gender_choice)
    flatno = models.CharField(('flatno'), max_length=128)
    street = models.CharField(('street'), max_length=128, blank=True)
    country = CountryField(blank=True)
    img = models.ImageField(upload_to = "images/")
    

    def __str__(self):
        return self.email
    
    
    
    
    
    
    
    
    
    
