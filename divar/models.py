from django.db import models
from django.contrib.auth.models import User









class Home_Model_buy(models.Model):

    addes = models.CharField(max_length=200)
    LenHome = models.IntegerField()
    Floor = models.IntegerField()
    Price = models.IntegerField()
    kabinet =  models.BooleanField()
    Elevator = models.BooleanField()
    Parking = models.BooleanField()
    Img_main = models.ImageField(upload_to='media/')
    Img_1 = models.ImageField(upload_to='media/',blank=True,null=True)
    Img_2 = models.ImageField(upload_to='media/',blank=True,null=True)
    Img_3 = models.ImageField(upload_to='media/',blank=True,null=True)
    yournum = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.addes
    
    
    
class Home_Model_Rent(models.Model):
    addes = models.CharField(max_length=200)
    LenHome = models.IntegerField()
    Floor = models.IntegerField()
    Price_First = models.IntegerField()
    Price_month = models.IntegerField()
    kabinet =  models.BooleanField()
    Elevator = models.BooleanField()
    Parking = models.BooleanField()
    Img_main = models.ImageField(upload_to='media/')
    Img_1 = models.ImageField(upload_to='media/',blank=True,null=True)
    Img_2 = models.ImageField(upload_to='media/',blank=True,null=True)
    Img_3 = models.ImageField(upload_to='media/',blank=True,null=True)
    yournum = models.CharField(max_length=100)

    
    def __str__(self) :
        return self.addes
