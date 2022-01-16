from django.shortcuts import render
import string    
import random 

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    uppercase = request.GET.get('uppercase', False)
    numbers = request.GET.get('numbers', False)
    length = int(request.GET.get('length', 12))
    choices = string.ascii_lowercase
    if uppercase:
        choices = choices + string.ascii_uppercase
    if numbers:
        choices = choices + string.digits
    userPassword = ''.join(random.choices(choices, k = length))    
    return render(request, 'generator/password.html', {'password': userPassword})

def about(request):
    return render(request, 'generator/about.html')