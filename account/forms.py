from django import forms
from django.contrib.auth.models import User
from city.models import City

class RegisterForms(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "first name"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "last name"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "email address"}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "user name"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),required=True,
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "city"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("نام کاربری وارد شده موجود می باشد")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("ایمیل وارد شده موجود می باشد")
        return email


class LoginForms(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "username or email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"}))