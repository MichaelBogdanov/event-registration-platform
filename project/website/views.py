from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout



def login_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return wrapper

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    
    data = {
        'form': form
    }

    return render(request, 'registration/login.html', data)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        print(form.errors)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile/')
    else:
        form = CustomUserCreationForm()

    data = {
        'form': form
    }

    return render(request, 'registration/register.html', data)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    data = {

    }
    return render(request, "profile.html", data)