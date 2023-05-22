from django.shortcuts import render,redirect
from .form import UserForm
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home(request):
    template_name="finalapp/Navbar.html"
    return render(request,template_name)

@login_required(login_url="logged")
def Register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("data")
    form=UserForm()
    template_name="finalapp/Register.html"
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url="logged")
def Data(request):
    obj=User.objects.all()
    template_name="finalapp/Data.html"
    context={'obj':obj}
    return render(request,template_name,context)

def Delete(request,id):
    obj=User.objects.get(id=id)
    obj.delete()
    return redirect("data")

def Update(request,id):
    obj=User.objects.get(id=id)
    if request.method=="POST":
        form=UserForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("data")
    form=UserForm(instance=obj)
    template_name="finalapp/Update.html"
    context={'form':form}
    return render(request,template_name,context)

def SignUp(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("logged")
    template_name="finalapp/Signup.html"
    context={'form':form}
    return render(request,template_name,context)

def Logged(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials!")
    template_name="finalapp/Login.html"
    return render(request,template_name)

def Log_Out(request):
    logout(request)
    return redirect("logged")
