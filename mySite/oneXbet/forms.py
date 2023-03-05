from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from oneXbet.models import Betting


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'login'}))
    password1 = forms.CharField(label='Пароль ',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='confirm',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm'}))
    email = forms.EmailField(label='email  ',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class BettingForm(forms.ModelForm):
    # game = forms.ChoiceField()
    # club = forms.ChoiceField()
    # money = forms.IntegerField(label='money')

    class Meta:
        model = Betting
        fields = ('money', 'club', 'game', 'url')


class ContactForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'enter', 'cols': 30, 'rows': 1, "placeholder": "message"}))
    admin_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'enter', "placeholder": "Enter your email"}))

# class="enter" placeholder="Enter your email" type="email" name="Enter your email"
# https://stackoverflow.com/questions/16079299/getting-init-got-an-unexpected-keyword-argument-instance-with-createview  #ctacko, example forms
