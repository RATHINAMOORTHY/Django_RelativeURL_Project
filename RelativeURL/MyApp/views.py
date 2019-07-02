from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'MyApp/index.html')

def about(request):
    return render(request,'MyApp/base.html')

def careers(request):
    return render(request,'MyApp/careers.html')
