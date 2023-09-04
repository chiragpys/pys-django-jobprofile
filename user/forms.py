from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         widgets = {"password": forms.PasswordInput()}


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class CreateStaffForm(forms.Form):
    user = forms.Select(choices=User.objects.all().values_list('id', flat=True))
    is_manager = forms.BooleanField()
    is_agent = forms.BooleanField()


