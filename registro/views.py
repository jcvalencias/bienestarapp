from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm, CreateUserForm


def registro(request):

    return render(request, 'index.html')


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'register.html', context)

def login(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'login.html', context)