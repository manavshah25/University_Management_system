from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# def login(request):
#     return render(request,"login.html")

def signup(request) :
     if request.method == "GET":
        return render(request,"sign_up.html")
     if request.method == "POST":
        username = request.POST['uname']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pwd']
        pass2 = request.POST['re-pwd']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Login')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Login')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('Login')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Login')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('Login')
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        # myuser.is_active = False
        # myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('Login')
    
def Login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        pass1 = request.POST['pwd']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
           
              login(request,user)
              fname = user.username
              superuser = user.is_superuser
              firstname= user.first_name
              context= {'fname' :fname,'superuser' :superuser,'firstname' : firstname}
         
            # messages.success(request, "Logged In Sucessfully!!")
              return redirect('index')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('Login')
    
    return render(request, "login.html")   
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Login')