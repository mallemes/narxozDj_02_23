from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин  ',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'login'}))
    password1 = forms.CharField(label='Пароль ',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='confirm',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm'}))
    email = forms.EmailField(label='email  ',
                                widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))

    #  class="form-control" placeholder="Confirm Password"
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')