from django.shortcuts import render

# Create your views here.

def add(request):
    return render(request,"add.html")

def recipe_list(request):
    return render(request,"recipes.html")

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")


