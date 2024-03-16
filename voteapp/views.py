from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
# arr = ['java','python','c', 'javascript', 'php','swift']
globalcnt = {'java': 0,'python': 0,'c': 0, 'javascript': 0, 'php': 0,'swift': 0}

def index(request):
    mydict = {
        "arr" : globalcnt
    }
    # return  HttpResponse("welcome to voting app")
    return render(request,'voteapp\index.html',context=mydict)

def getquery(request):
    q = request.GET['query']
    if q in globalcnt:
        # if already exist then increment the value
        globalcnt[q] = globalcnt[q]+1
    else:
        #first occurance
        globalcnt[q]=1
    dict = {
        "arr" : globalcnt
    }
    return render(request,'voteapp\index.html', context=dict)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(), key= lambda x:x[1], reverse=True))
    mydict = {
        "arr" : globalcnt
    }
    return render(request,'voteapp\index.html', context=mydict)
