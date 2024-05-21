from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class registrationfrom(UserCreationForm):
    Email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = {'username','first_name','last_name'}
        


class loginform(AuthenticationForm):
    class Meta:
        model = User
        fields ='__all__'
    