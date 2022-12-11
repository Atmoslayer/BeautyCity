from django import forms
from django.contrib.auth.models import User

from .models import *
from django.contrib.auth.forms import AuthenticationForm


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label='Пароль', strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    username = forms.CharField(
        label='Логин',
    )
    password = forms.CharField(
        label='Пароль',
    )
    email = forms.EmailField(
        label='Почта',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input'

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user