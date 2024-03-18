from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')
    
def LoginPage(request):
    return render(request, 'login.html')
    
def RegisterPage(request):
    return render(request, 'cadastro.html')
    