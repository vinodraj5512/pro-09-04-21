from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def great(request):
    return render(request,"sample.html",context={'a':100,'b':10})

def if_demo(request):
    login=True
    return render(request,"if_demo.html",context={'login':login})

def for_demo(request):
    return render(request,"for_demo.html",context={'items':['apple','ball','cat','dog'],'profile':{'name':'vinod','age':24,'sal':30000}})