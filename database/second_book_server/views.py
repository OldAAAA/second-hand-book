from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from second_book_server.models import User


def registe(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        data = request.POST.copy()
        email = data.get('email')
        username = data.get('nickname')
        password = data.get('password')
        university = data.get('university')
        print(email)
        find_same = User.object.filter(email = email)
        print(find_same)
        if len(find_same) > 0:
            return render(request,'register.html')
        else:
            User.object.create_user(email = email,username=username,password = password,university=university)
            return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.get('password')
        is_user = User.object.filter(email = email)
        if is_user:
            user = authenticate(email=email, password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,'index.html')
            else:
                return render(request,'login.html')
        else:
            return render(request, 'login.html')

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    return HttpResponse('OK')