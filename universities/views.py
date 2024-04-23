from django.shortcuts import render

def HomeView(request):
    return render(request, 'universities/index.html')


def Login(request):
    return render(request, 'user/login.html')

def Signup(request):
    return render(request, 'user/signup.html')