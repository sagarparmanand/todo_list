from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'account/login.html')
    
    def post(self,request):
            context={}
            uname=request.POST['uname']
            upass=request.POST['upass']

            if uname=='' or upass=='':
                context['errmsg']="Fields cannot be empty..."
                return render(request,'account/login.html',context)
            else:
                u=authenticate(username=uname,password=upass)

                if u is not None:
                    login(request,u)
                    return redirect('/')

                else:    
                    context['errmsg']="invalid username and password..."
                    return render(request,'account/login.html',context)    

class Register(View):
    def get(self,request):
        return render(request,'account/register.html')
    
    def post(self,request):
        context={}
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']

        if uname=='' or uemail=='' or upass=='' or ucpass=='':
            context['errmsg']="Fields cannot be empty..."
            return render(request,'account/register.html',context)
        elif len(upass)<=5:
            context['errmsg']="Password must be in 6 character"
            return render(request,'account/register.html',context)
        elif upass != ucpass:
            context['errmsg']="Password not matched..."
            return render(request,'account/register.html',context)
        else:
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass)
            u.save()
            context['success']="Registered successfully..."
            return render(request,'account/register.html',context)


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/')