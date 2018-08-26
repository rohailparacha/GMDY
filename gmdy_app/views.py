from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

#@login_required
def home(request):
    return render(request,'gmdy_app/home.html')

def loginn(request):
    users = User.objects.all()
    print(users)
    return HttpResponse(users)

def login(request):
    user = None
    if request.method == 'POST':
        username=request.POST.get('email')
        password=request.POST.get('pass')
        try:
            user = User.objects.get(username=username)
            if user is not None and user.is_active:
                if user.check_password(password):
                    login(request,user)
                    return redirect('home')
                else:
                    return HttpResponse('incorrect password')
            else:
                return HttpResponse('check credentials')
        except:
            return redirect('login')
    return render(request,'gmdy_app/login.html')

                    
