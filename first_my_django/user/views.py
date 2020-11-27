from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout(request):
    logout_user(request)
    messages.success(request, 'You Successfully Log out')
    return redirect(reverse('login'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            logins = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if logins:
                login_user(request,logins)
                messages.success(request, 'You Successfully Log In %s' % form.cleaned_data.get('username'))
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Username or Password is Wrong')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {
        'form': form
    })


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You has been create new account %s' % form.cleaned_data.get('username'))
            return redirect(reverse('login'))
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {
        'form': form
    })