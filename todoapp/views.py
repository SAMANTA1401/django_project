from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from .models  import *  #import all models here
import datetime

# Create your views here.
def  index(request):
    return render(request, 'todoapp\index.html')

def submit(request):
    obj = Todo() #imort from model.py class Todo()
    obj.title = request.GET['title']
    obj.description=request.GET['desc']
    obj.priority = request.GET['prior']
    obj.save()
    mydict = {
        "alltodos" : Todo.objects.all(),
    }
    print(Todo.objects.all())
    print(obj.created_at)
    return render(request,'todoapp\list.html',context=mydict)

def lists(request):
    mydict = {
        "alltodos" : Todo.objects.all(),
    }
    return render(request,'todoapp\list.html' , context=mydict) 

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydict = {
        "alltodos" : Todo.objects.all(),
    }
    return render(request,'todoapp\list.html' , context=mydict)
    # return redirect(lists)

def sortdata(request):
    mydict = {
        # "alltodos" : Todo.objects.all().order_by('-created_at'),
        "alltodos" : Todo.objects.all().order_by('priority'),

    }
    return render(request,"todoapp\list.html" ,context=mydict)


def searchdata(request):
    q = request.GET['query']
    mydict={
        "alltodos" : Todo.objects.filter(title__contains=q)
    }
    return render(request, 'todoapp\list.html', context=mydict)

def edit(request,id):
    obj = Todo.objects.get(id=id)
    dict = {
        "title" : obj.title,
        "description":obj.description,
        "priority":obj.priority,
        "id" : obj.id
    }
    print(dict['id'])
    return render(request,'todoapp\edit.html',context=dict)

def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['desc']
    obj.priority = request.GET['prior']
    obj.created_at = datetime.datetime.now()
    obj.save()
    mydict = {
        "alltodos" :Todo.objects.all()
    }
    return render(request,"todoapp\list.html" ,context=mydict)

