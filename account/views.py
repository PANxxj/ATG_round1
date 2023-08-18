from django.shortcuts import redirect, render
from .models import *
from .forms import  *
from django.contrib.auth import authenticate,login,logout


def signUp(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST,request.FILES)
        email=request.POST.get('email')
        password = request.POST.get('password1')
        repeat_password = request.POST.get('password2')
        if password and repeat_password and password != repeat_password:
            return render(request,'signup.html',{"errors":'password does not match'})
        print(email)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(';;;;;;;;;;;;',form.errors)
            return render(request,'signup.html',{"error":form.errors,"form":form})
    else:
        return render(request,'signup.html',{'form':CustomUserCreationForm()}) 

def logIn(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=authenticate(request,email=email,password=password)
            if user:    
                print('user',user)
                login(request,user)
                return render(request,'dashboard.html',{'user':CustomUser.objects.get(email=email)})
        except CustomUser.DoesNotExist:
            return render(request,'login.html',{'error':'invalid email or password'})
    else:
        return render(request,'login.html')