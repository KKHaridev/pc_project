from django.shortcuts import render
from .models import hospitals

# Create your views here.
a = 'alappuzha'
def home(request):
    hospital = hospitals.objects.all()
    return render(request , 'base/index.html',{'hospitals' : hospital})

def register(request):
    return render(request , 'base/register.html')

def alappuzha(request):
    hospital = hospitals.objects.filter(district=a)
    return render(request , 'base/alappuzha.html',{'hospitals' : hospital})