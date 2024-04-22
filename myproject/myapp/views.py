from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    return render(req,"home.html")

def login(req):
    if req.method == 'POST':
        name=req.POST.get('username')
        password=req.POST.get('password')
        if not User.objects.filter(username=name).exists():
            messages.info(req,"Invalid User")
            redirect("/login.html")
        else:
            user=authenticate(username=name,password=password)
            if user is None:
                messages.info(req,"Invalid Password")
            else:
                auth.login(req,user)
                return redirect("home.html ")
    return render(req,'login.html')

def signup(req):
    if req.method == 'POST':
        name=req.POST.get("username")
        password=req.POST.get("password")
        email=req.POST.get("email")
        user=User.objects.filter(username=name)
        if user.exists():
            messages.info(req,'User Already Exist')
            redirect("/signup.html")
        else:
            user=User.objects.create_user(
                username=name,
                email=email
            )
            user.set_password(password)
            user.save()
            messages.info(req,"Signup Successful")
    return render(req,'signup.html')


@login_required
def addBook(req,user_id):
    pass

def logout(req):
    auth.logout(req)
    return redirect("home.html")