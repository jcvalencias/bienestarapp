from django.shortcuts import render

def registro(request):

    return render(request, 'index.html')
    

def register(request):

    return render(request, 'register.html')

def login(request):

    return render(request, 'login.html')