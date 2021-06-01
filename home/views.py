
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')    

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact= Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(request, "Your message has been sent")
    return render(request, "home/contact.html")


def handlesignup(request):
    if request.method=="POST":
        username = request.POST['username']
        firstname = request.POST['firstname'] 
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)>10:
            messages.error(request, "Your username must be under 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username must contain alphabets and numbers")
            return redirect('/')
        if pass1 !=  pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.firstname= firstname
        myuser.lastname= lastname
        myuser.save()
        messages.success(request, "Your account has been created")
        return redirect('/')    
    else:
        return HttpResponse('404 - Not Found')    

def handlelogin(request):
    if request.method== "POST":
        loginusername= request.POST['loginusername']
        loginpassword= request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect("/")
    return HttpResponse('login')    
    return HttpResponse('login')    

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully lgged out")
    return redirect("/")
