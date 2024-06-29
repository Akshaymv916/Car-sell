from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Brand(models.Model):
    brand_name=models.CharField(max_length=200)
    brand_image=models.ImageField(null=True)

    def __str__(self):
        return self.brand_name

class Fueltype(models.Model):
    fuel=models.CharField(max_length=200)
    def __str__(self):
        return self.fuel

class Color(models.Model):
    color_name=models.CharField(max_length=100)
    def __str__(self):
        return self.color_name
    






class Car_details(models.Model):


    car_name=models.CharField(max_length=200)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    fuel_type=models.ForeignKey(Fueltype,on_delete=models.CASCADE)
    price=models.CharField(max_length=100)
    image1=models.ImageField()
    image2=models.ImageField()
    image3=models.ImageField()
    image4=models.ImageField()
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    year=models.IntegerField()
    kilometer=models.IntegerField()
    owners=models.IntegerField()
    features=RichTextField(null=True)

    def __str__(self):
        return self.car_name
    
    

class call_request(models.Model):
    owner_user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name


class Car_sell(models.Model):

    STATUS=[
        ('Reject','Reject'),
        ('accept','Accept'),
    ]

    status=models.CharField(max_length=60,choices=STATUS,default=STATUS[0])
    owner_user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    seller_name=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    car_name=models.CharField(max_length=200)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    fuel_type=models.ForeignKey(Fueltype,on_delete=models.CASCADE)
    price=models.CharField(max_length=100)
    image1=models.ImageField()
    image2=models.ImageField()
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    year=models.IntegerField()
    kilometer=models.IntegerField()
    owners=models.IntegerField()
    features=RichTextField(null=True)
    def __str__(self):
        return f"{self.car_name}----{self.owner_user}"