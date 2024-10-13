from django.shortcuts import redirect, render
from .models import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.



def login_page(request):
    #form submission
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        #check if the user provided data exist
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect("/login/")
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')
        
    return render(request,"login.html")

def register(request):

    if request.method=="POST":
        
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username already Taken")
            return redirect('/register/')
        
        # Create a new User object with the provided information
        user = User.objects.create (
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        messages.info(request,"Successfully registerd")
        
        return redirect('/register/')

    return render(request,"register.html")        
    

def add(request):
    if request.method=='POST':
        data=request.POST

        recipe_name=data.get("recipe_name")
        recipe_dis=data.get("recipe_dis")
        recipe_image=request.FILES.get( "recipe_image")
        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_dis=recipe_dis,

        )
        return redirect('/add/')
    queryset=Recipe.objects.all()

    context={'recipes':queryset}

    return render(request,"add.html",context)



def recipe_list(request):
    qureyset=Recipe.objects.all()
    context={'recipes':qureyset}
    return render(request,"recipes.html",context)

def home(request):
    return render(request,"index.html")




