from django.shortcuts import render



def Sign_upview(request):
    return render(request, 'index.html')

def LoginView(request):
    return render(request, 'login.html')