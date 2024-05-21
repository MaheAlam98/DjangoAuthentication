from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('registration/',views.registration,name='registrationpage'),
    path('login/',views.userlogin,name='loginpage'),
    path('profile/',views.profile,name='profilepage'),
    path('logout/',views.userlogout,name='logout'),
    path('changepassword/',views.user_change_password,name='user_change_password'),
]
