from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from divar.views import PassView,Panel_View,Home_View,RENT,BUY,About,get_buy,Profile_View,get_rent,conme,Select,rent_model_user,buy_model_user,Register,LoginUser,LogOutUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', Home_View),
    path('rent', RENT),
    path('buy', BUY),
    path('About', About),
    path('conme', conme),
    path('rentdet<int:id>',get_rent),
    path('buydet<int:id>',get_buy),
    path('sel',Select),
    path('rentcreate',rent_model_user),
    path('buycreate',buy_model_user),
    path('sigin',Register),
    path('login',LoginUser),
    path('logout',LogOutUser),
    path('pan',PassView),
    path('profile',Profile_View),
    path('Panel_View',Panel_View),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #not both
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)