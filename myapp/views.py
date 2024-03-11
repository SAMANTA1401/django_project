from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse

# Create your views here.
#2. go to settings.py
def myfunctioncall(request):
    return HttpResponse("hello world")
    

def myfunctioncallabout(request):
    return HttpResponse("about hello world")

def add(request,a,b):
    return HttpResponse(a+b)

# def intro(request,name,age):
#     return HttpResponse(f"{name}'s age is {age}")

def intro(request,name,age):
    mydict = {
        "name": name,
        "age" : age
    }
    return JsonResponse(mydict)

def index(request):
    return render(request,'index.html')
