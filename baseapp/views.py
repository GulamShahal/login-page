from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate
# from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, "baseapp/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad credential")
            # return render(request,"baseapp/index.html")
    return render(request, "baseapp/signin.html")


@login_required(login_url='/signin')
def home(request):
    return render(request, "baseapp/index.html")


def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully")
    return redirect("signin")
