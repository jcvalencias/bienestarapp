from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm, CreateUserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')


        context = {'form': form}

        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {}

        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'login.html', context)

        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homePage(request):
    username = 'Juan'
    context = {'username' : username}
    return render(request, 'index.html', context = context)