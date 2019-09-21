from django.shortcuts import render
from .models import  JOb
def home(request):
    jobs = JOb.objects
    return render(request,'jobs/home.html',{'jobs':jobs})

# Create your views here.
