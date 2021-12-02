from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member
# Create your views here.

def index(request):
    if request.method == 'POST':
        member = Member(Email=request.POST['Email'], Password=request.POST['Password'], Username=request.POST['Username'], Name=request.POST['Name'],Address=request.POST['Address'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if Member.objects.filter(Email=request.POST['Email'], Password=request.POST['Password']).exists():
            member = Member.objects.filter(Email=request.POST['Email'],Password=request.POST['Password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)

