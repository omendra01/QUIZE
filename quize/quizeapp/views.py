from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from .models import *

def index(request):
    return render(request,'index.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password =make_password(request.POST.get('password'))
        user = User(username=name,email=email,password=password)
        if User.objects.filter(username=name).exists():
            messages.info(request,'User already registere..')
            return redirect('register')
        x = Register(mobile=mobile)
        user.save()
        x.save()
    return render(request,'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('instruction')
        messages.info(request,'Invalid Details')
        return render(request,'login.html')    
    return render(request,'login.html')  


def quizetest(request):
    obj = QuizeQuestion.objects.all()[:10]
    return render(request,'quizetest.html',{'obj':obj})  

def result(request):
    if request.method=='POST':
        correct = 0
        question = QuizeQuestion.objects.all()
        for q in question:
            print('selected question',request.POST.get(q.question))
            print(q.answer)
            if q.answer== request.POST.get(q.question):   
                correct+=1   
        context ={'correct':correct} 
        return render(request,'result.html',context) 
    return render(request,'result.html',context)                      



def instruction(request):
    return render(request,'instruction.html')
   