from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def calui(request):
    return render(request, 'calapp\calui.html')

def submitquery(request):
    q = request.GET['query']
    # jsondict = {
    #     "q" : q

    # }
    # return JsonResponse(jsondict)
    # return  HttpResponse(q)
    try:
        ans = eval(q)
        mydict = {
            "q" : q,
            "ans" : ans,
            "error" : False
        }
        return render(request,'calapp\calui.html', context=mydict)
    except:
        mydict = {
            "error" : True
        }
        return render(request,'calapp\calui.html', context=mydict)
