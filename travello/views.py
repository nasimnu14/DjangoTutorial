from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
 
# Create your views here.

def index(request):
    dest1=Destination()
    dest2=Destination()
    dest3=Destination()

    dest1.description="This is not a googd place"
    dest1.name="Dhaka"
    dest1.price=1000
    dest1.img="destination_1.jpg"
    dest1.offer=False
    
    dest2.name="Chottagram"
    dest2.description="Very bad"
    dest2.price=1500
    dest2.offer=True
    dest2.img="destination_2.jpg"

    dest3.name="B-Baria"
    dest3.description="Very Overall"
    dest3.price=100
    dest3.offer=False
    dest3.img   ="destination_3.jpg"
    dests=[dest1,dest2,dest3]

    return render(request,"index.html",{'dests':dests})
