from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserRgisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class Search_Form(forms.ModelForm):
        class Meta:
            model = Home_Model_buy
            fields = ['addes']




class buy_Form(forms.ModelForm):
        class Meta:
            model = Home_Model_buy
            fields = ['addes','LenHome','Floor','Price','kabinet','Elevator','Parking','Img_main','Img_1','Img_2','Img_3']
            
            
            

class rent_Form(forms.ModelForm):
        class Meta:
            model = Home_Model_Rent
            fields = ['addes','LenHome','Floor','Price_First','Price_month','kabinet','Elevator','Parking','Img_main','Img_1','Img_2','Img_3']




class passForm(forms.ModelForm):
        class Meta:
            model = Home_Model_buy
            fields = ['addes']
