from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import extenduser
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import memory
from math import ceil


# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request,'blog/home.html',{'posts':posts})


def about(request):
    return render(request,'blog/about.html')
@login_required(login_url='/login/')
def add(request):
    if request.method=="POST":
        data=request.POST['data']
        new=memory(content=data,user=request.user)
        new.save()
        return render(request,'blog/add.html')
    else:
        return render(request,'blog/add.html')



def signin(request):
    if request.method=='POST':
        if request.POST['pass']==request.POST['passagain']:
            try:
                user=User.objects.get(username=request.POST['user'])
                return render(request,'blog/signin.html',{'error':"username has already taken"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['user'],password=request.POST['pass'])
                phnum=request.POST['phone']
                age=request.POST['age']
                newextenduser=extenduser(phone_num=phnum,age=age,user=user)
                newextenduser.save()
                auth.login(request,user)
                return render(request,'blog/login.html')
        else:
            return render(request,'blog/signin.html',{'error':"password not match"})
        
    else:
        return render(request,'blog/signin.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['user']
        pwd=request.POST['pass']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(dashboard)
        else:
            return render(request,'blog/login.html',{'error':"Invalid Login Credintials."})
        
    else:
        return render(request,'blog/login.html')
                          
        
def logout(request):
    auth.logout(request)
    return redirect(home)

def showuserdata(request):
    datas=extenduser.objects.filter(user=request.user)
    return render(request,'blog/showbar.html',{'data':datas})
@login_required(login_url='/login/')
def dashboard(request):
    log_user=request.user
    memories=memory.objects.filter(user=log_user)
    return render(request,'blog/dashboard.html',{'m':memories})


