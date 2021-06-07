from django.shortcuts import render
from .models import hospitals

# Create your views here.

def home(request):
    hospital = hospitals.objects.all()
    return render(request , 'base/index.html',{'hospitals' : hospital})

def register(request):
    return render(request , 'base/register.html')

def district(request, disid):
    hospital = hospitals.objects.all()
    if disid == 1 :
        return render(request , 'base/district.html', {'hospitals' : hospital, 'id' : disid , 'name' : 'ALAPPUZHA'} )