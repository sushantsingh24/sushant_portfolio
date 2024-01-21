from django.http import HttpResponse
from django.shortcuts import render,redirect 
from django.http import FileResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url="/login")
def resume(request):
    try:
        return FileResponse(open('Sushant resume .pdf', 'r'), content_type='pdf')
    except FileNotFoundError:
        raise Http404()

def home(request):
    data={
        'title':'Sushant_singh24'
    }
    return render(request,"index.html",data)
@login_required(login_url="/login")
def achivement(request):
    data={
        'title':'Achivement'
    }
    return render(request,"achivement.html",data)

def loginPage(request):
    data={
        'title':'Login'

    }
  
    if request.method=='POST':
        user=request.POST.get("Username")
        pass1=request.POST.get("Password")

        user=authenticate(request,username=user,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
            messages.success(request,"you seccessfully login")
      
        else:
            return HttpResponse ("Username or password incorrect")

    return render(request,"login.html",data)
def signup_page(request):
    data={
        'title':'Signup'
    }
    if request.method=='POST':
        uname=request.POST.get("username")
        number=request.POST.get("number")
        email=request.POST.get("email")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")


        my_user=User.objects.create_user(uname,email,password)
        my_user.save
            
        return redirect('login')
    return render(request,"signup.html",data)


def logoutPage(request):
    logout(request)
    return redirect('home')