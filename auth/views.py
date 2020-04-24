from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import auth

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'accounts/login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')