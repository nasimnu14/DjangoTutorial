from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    x=16+12
    return render(request,"home.html",{'name':x})
def add(request):
    
    x=request.POST["num1"]
    x+=request.POST["num2"]
    
    return render(request,"result.html",{"result":x})
