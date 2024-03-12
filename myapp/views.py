from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from  .forms import *
import re

# Create your views here.
#2. go to settings.py
def error_404_view(request,exception):
    return render(request,'404.html')

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

def home(request):
    return render(request,'home.html')

def first(request):
    var = "hello"
    mssg = "hey  there!"
    fruits = ["apple","banana","mango"]
    num1, num2 = 3,5
    ans = num1>num2
    # print(ans)
    mydict2 = {
        "var" : var,
        "greeting" : mssg,
        "fruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request,'first.html',context=mydict2)

def imagepage(request):
    return render(request,"image.html")

def imagepage2(request,imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    # print(myimagename)
    if myimagename == 'django':
        var = True
    elif  myimagename == 'python':
        var = False
    mydict3 = {
        "var" : var
    }
    return render(request,"image2.html", context=mydict3)

def myform(request):
    return render(request,'myform.html')

def submitform(request):
    mydict4 = {
        "var1" :  request.POST['emailval'],
        "var2" : request.POST['passwordval'],
        "method" : request.method
    }
    return JsonResponse(mydict4)
    ## 2:19:41

def myform2(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = request.POST['email'],
            password = request.POST['password']
            print(email)
            print(password)
            mydict6 = {
                "form" : FeedbackForm(),
                # "success" : True,
                # "successmsg" : "Form Submitted"
            }
            errorflag = False
            Erros = []
            if str(email) != str(email).lower():
                errorflag = True
                errormsg = "email should be in smaller"
                # return render(request,'myform2.html',context=mydict6)
                Erros.append(errormsg)
                # print(Erros)
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.fullmatch(regex,str(email)):
                errorflag = True
                errormsg = "Not a vlid email id"
                Erros.append(errormsg)
            if errorflag != True:
                mydict6["success"] =True
                mydict6["successmsg"] = "form submitted successfully"
            print(errorflag)

            mydict6["error"] = errorflag
            mydict6["errors"] = Erros
            print(mydict6['errors'])

            return render(request,'myform2.html',context=mydict6)

                
            # var = str("Form submitted successfully" + str(request.method))
            # return HttpResponse(var)
        else:
            mydict5 = {
                "form" :  form,
            }
            return render(request,'myform2.html',context=mydict5)

    elif request.method == 'GET':
        form = FeedbackForm() # create an empty form (a blank slate) from forms.py froms .form import * 
        mydict5 = {
            "form" : form
        }
        return render(request,'myform2.html',context=mydict5)