from django.shortcuts import render,redirect
# Create your views here.
from .models import *
def home(request):
    return render(request,'index.html',{})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=User_Register(username=username,email=email,password=password)
        user.save()
        return redirect('home')
    return render(request,'register.html')