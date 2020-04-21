from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import ImgPlace, NamesPlace
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    return render(request,"home.html",context)

def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/persius")
        else:
            messages.info(request, "Incorrect! Username or Password!")
            return redirect("/persius/login")
    else:
        if request.user.is_authenticated:
            return redirect("/persius")
        else:
            return render(request,"login.html",context)

def signup(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["re_password"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("User already exist!")
                messages.info(request,"User already exist!")
                return redirect("/persius/signup")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User created!")
                messages.info(request, "User created!")
                return redirect("/persius/login")
        else:
            messages.info(request, "Password Mismatched!")
            return HttpResponseRedirect(request.path_info)
    else:
        if request.user.is_authenticated:
            return redirect("/persius")
        else:
            return render(request,"signup.html",context)

def logout(request):
    auth.logout(request)
    return redirect("/persius/")

@login_required
def place(request):
    print("===================")
    print(request.FILES)
    im = request.FILES['image']
    name = request.POST['place_name']
    # user = request.user.username
    print(im)
    print(name)
    # print(user)
    places = NamesPlace(names=name)
    places.save()
    img_place = ImgPlace(img=im, place=name)
    img_place.save()
    return render(request, "home.html")