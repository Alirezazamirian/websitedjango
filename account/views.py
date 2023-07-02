from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForms, RegisterForms
from django.contrib import messages
from django.contrib.auth import login, authenticate

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_forms = LoginForms(request.POST or None)
    if login_forms.is_valid():
        username = login_forms.cleaned_data.get('user_name')
        password = login_forms.cleaned_data.get('password')
        if '@' in username:
            check_email = User.objects.filter(email__exact=username).first()
            if check_email:
                username = check_email.username
            else:
                username = None
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'{user.first_name} ورود شما با موفقیت انجام شد ')
            return redirect('/')
        else:
            login_forms.add_error('user_name', 'کاربری با این مشخصات وجود ندارد')
    context = {
        "login_form": login_forms
    }
    return render(request, "account/login.html", context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_forms = RegisterForms(request.POST or None)
    context = {
        "register_form": register_forms
    }
    if register_forms.is_valid():
        context["register_form"] = RegisterForms()
        first_name = register_forms.cleaned_data.get('first_name')
        last_name = register_forms.cleaned_data.get('last_name')
        email = register_forms.cleaned_data.get('email')
        username = register_forms.cleaned_data.get('username')
        city = register_forms.cleaned_data.get('city')
        password = register_forms.cleaned_data.get('password')
        new_user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        profile = Profile.objects.create(user=new_user, city=city)
        login(request, new_user)
        messages.success(request, 'ثبت نام شما با موفقیت انجام شد')
        return redirect('/')

    return render(request, 'account/register.html', context)