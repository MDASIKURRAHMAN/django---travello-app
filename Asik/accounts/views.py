from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
def register(request):
    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if (password == confirm_password):
            
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect(request,'register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect(request,'register')
            else:
            
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                print("user created")
            return redirect('login')
            

        else:
            print ("password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render (request,'register.html')

def login (request):
    if request.method=='POST':
        username = request.POST['username']
        passcode = request.POST['password']
        user=auth.authenticate(username=username, password=passcode)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credintials')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

