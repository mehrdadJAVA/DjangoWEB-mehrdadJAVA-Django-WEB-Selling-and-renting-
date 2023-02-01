from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User







# home view and search
def Home_View(request):
    Data = ''
    Rent = Home_Model_Rent.objects.all()
    form = Search_Form
    if request.method == 'POST':
        form = Search_Form(request.POST)
        if form.is_valid():
            for i in form:
                Data = i.data
            print(Data)
            try :
                rent = Home_Model_Rent.objects.filter(addes = Data)
                buy = Home_Model_buy.objects.filter(addes = Data)
                if rent or buy :
                    return render(request,'divar/search.html',{'buy':buy,'rent':rent})
                else:
                    return render(request,'divar/resie.html',{})
            except:
                    return render(request,'divar/resie.html',{})

    
    model = {'rent':Rent,'form':form}
    return render(request,'divar/index.html',model)



# login 
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is  not None:
            login(request,user)
            return redirect(Home_View)
        else:
            return render(request,'divar/loginerror.html',{})
    return render(request,'divar/login.html',{})
        

# register django 
def Register(request):
    form = UserRgisterForm()
    
    if request.method == 'POST':
        form = UserRgisterForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(LoginUser)
        else:
            return render(request,'divar/registererror.html',{})

    return render(request,'divar/sigin.html',{'form':form})




def  Select(request):
    return render(request,'divar/select.html',{})
    


#logout
def LogOutUser(request):
    logout(request)
    return redirect(Home_View)




def rent_model_user(request):
    List = []
    form = rent_Form
    if request.method == 'POST':
        form = rent_Form(request.POST,request.FILES)
        if form.is_valid():
            for i in form:
                List.append(i.data)
            user=str(request.user.id)
            model = Home_Model_Rent(addes=List[0],LenHome=List[1],Floor=List[2],Price_First=List[3],Price_month=List[4],kabinet=List[5],Elevator=List[6],Parking=List[7],
                                    Img_main=List[8],Img_1=List[9],Img_2=List[10],Img_3=List[11],yournum=user)
            model.save()
            print('save')
            return render(request,'divar/sucmsg.html',{})
    return render(request,'divar/rentmodel.html',{'form':form})




def buy_model_user(request):
    List = []
    form = buy_Form
    if request.method == 'POST':
        form = buy_Form(request.POST,request.FILES)
        if form.is_valid():
            for i in form:
                List.append(i.data)
            user=str(request.user.id)
            model = Home_Model_buy(addes=List[0],LenHome=List[1],Floor=List[2],Price=int(List[3]),kabinet=List[4],Elevator=List[5],Parking=List[6],
                                    Img_main=List[7],Img_1=List[8],Img_2=List[9],Img_3=List[10],yournum=user)
            model.save()
            print('save')

            return render(request,'divar/sucmsg.html',{})
    return render(request,'divar/buymodel.html',{'form':form})



#rent view
def RENT(request):
    Rent = Home_Model_Rent.objects.all()
    model = {'rent':Rent}
    return render(request,'divar/rent.html',model)


#buy view
def BUY(request):
    buy = Home_Model_buy.objects.all()
    model = {'buy':buy}
    return render(request,'divar/buy.html',model)


# about view
def About(request):
    return render(request,'divar/about.html',{})


# ditel  buy home view
def get_buy(request , id):
    kabinet = ''
    asansor = ''
    parking = ''
    buy = Home_Model_buy.objects.get(id = id)
    
    if buy.Elevator == True:
        asansor = 'دارد'
    else:
        asansor = 'ندارد'
        
    if buy.kabinet == True:
        kabinet = 'دارد'
    else:
        kabinet = 'ندارد'      
    
    if buy.Parking == True:
        parking = 'دارد'
    else:
        parking = 'ندارد'  
    
    
    
    model = {'buy':buy,'parking':parking,'asansor':asansor,'kabinet':kabinet,'price':buy.Price}
    return render(request,'divar/buydet.html',model)



# ditel  rent home view
def get_rent(request , id):
    kabinet = ''
    asansor = ''
    parking = ''
    rent = Home_Model_Rent.objects.get(id = id)
    
    if rent.Elevator == True:
        asansor = 'دارد'
    else:
        asansor = 'ندارد'
        
    if rent.kabinet == True:
        kabinet = 'دارد'
    else:
        kabinet = 'ندارد'      
    
    if rent.Parking == True:
        parking = 'دارد'
    else:
        parking = 'ندارد'  
    
    
    model = {'rent':rent,'parking':parking,'asansor':asansor,'kabinet':kabinet,'price1':rent.Price_First,'price2':rent.Price_month}
    return render(request,'divar/rentdet.html',model)




def conme(request):
    return render(request,'divar/conme.html',{})



def Profile_View(request):
    user = User.objects.get(id=request.user.id)
    buy = Home_Model_buy.objects.filter(yournum = request.user.id)
    rent = Home_Model_Rent.objects.filter(yournum = request.user.id)
    print(user.username,user.email)
    con = {"username":user.username,'email':user.email,'rent':rent,'buy':buy}
    return render(request,'divar/profile.html',con)


# panel admin dont full 
def Panel_View(request):
    Counter = 0
    Counter_Buy = 0
    Counter_rent = 0
    user = User.objects.all()
    product1 = Home_Model_buy.objects.all()
    product2 = Home_Model_Rent.objects.all()
    
    for j in product1:
        Counter_Buy = Counter_Buy + 1
        
    for k in product2:
        Counter_rent = Counter_rent + 1
    
    for i in user:
        Counter = Counter + 1
    
    print(Counter,Counter_Buy,Counter_rent)
    contact = {'product1':product1,'product2':product2,'Counter_Buy':Counter_Buy,'Counter_rent':Counter_rent,'Counter':Counter}
    return render(request,'divar/panel.html',contact)
    
    



# panel View pass
def PassView(request):
    passWord = '09149236907'
    form = passForm
    if request.method == 'POST':
        form = passForm(request.POST)
        if form.is_valid():
            for i in form:
                if passWord == i.data:
                    return redirect(Panel_View)
                else:
                    return render(request,'divar/passerror.html',{})

    return render(request,'divar/pass.html',{'form':form})
            