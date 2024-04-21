from django.db import models
from django.contrib.auth.models import User



class Ngo(models.Model):
    name = models.CharField(max_length=160)
    email = models.CharField(max_length=100,default='email')
    password = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name



class Donated_food(models.Model):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    name = models.CharField(max_length=160)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=255)
    food_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Donation(models.Model):
    name = models.CharField(max_length=160)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=255)
    food_type_choice = (
        ('Raw', 'Raw'),
        ('Cooked', 'Cooked'),
    )
    food_type = models.CharField(max_length=100, choices=food_type_choice, blank=True, null=True)
    quantity = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name