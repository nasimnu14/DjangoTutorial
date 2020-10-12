from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):
    dest1=Destination()
    dest1.description="This is not a googd place"
    dest1.name="Dhaka"
    dest1.price=1000

    return render(request,"index.html",{'dest1':dest1})
