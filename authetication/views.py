from django.shortcuts import render,redirect
from . forms import registrationfrom, loginform,AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm,SetPasswordForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=='POST':
     fm=registrationfrom(request.POST)  
     if fm.is_valid():
         fm.save()
         messages.success(request,'Registration Successfully!!')
         return redirect('loginpage')
    else:      
      fm=registrationfrom()
    return render(request,'registration.html',{'form':fm})


def userlogin(request):
    if not request.user.is_authenticated:        
        if request.method=='POST':
            lf=AuthenticationForm(request=request,data=request.POST)
            if lf.is_valid():
                uname=lf.cleaned_data['username']
                upass=lf.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Login Successfully!!')
                    return redirect('profilepage') 
        else:            
          lf= loginform()
        return render(request,'login.html',{'loginfrom':lf})
    else:
        return redirect('profilepage')


def profile(request):
    if request.user.is_authenticated:   
      return render(request,'profile.html')
    else:
        return redirect('loginpage')


def userlogout(request):
    logout(request)
    return redirect('homepage')

# password change with old password
# def user_change_password(requst):
#     if requst.user.is_authenticated:
        
#         if requst.method=='POST':
#             fm=PasswordChangeForm(user=requst.user,data=requst.POST)
#             if fm.is_valid():
#                 fm.save()
#                 update_session_auth_hash(requst,fm.user)
#                 messages.success(requst,'Passwordchange sccessfull!!')
#                 return redirect('profilepage')
#         else:
#             fm=PasswordChangeForm(user=requst.user)
#         return render(requst,'changepassword.html',{'form':fm})

#     else:
#         return redirect('loginpage')

#password change without old password
def user_change_password(requst):
    if requst.user.is_authenticated:
        
        if requst.method=='POST':
            fm=SetPasswordForm(user=requst.user,data=requst.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(requst,fm.user)
                messages.success(requst,'Passwordchange sccessfull!!')
                return redirect('profilepage')
        else:
            fm=SetPasswordForm(user=requst.user)
        return render(requst,'changepassword.html',{'form':fm})

    else:
        return redirect('loginpage')