from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from main.models import Resources , StartUps , Schemes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Create your views here
def home(request):
    startups = StartUps.objects.all()
    context = {
        'startups': startups
    }
    return render(request , 'main/firstPage.html' , context)

def about(request):
    return render(request , 'main/about.html')

def govtSchemes(request):
    schemes = Schemes.objects.all()
    context = {
        'schemes': schemes,
    }
    return render(request , 'main/govtScheme.html' , context)

def reources(request):
    courses = Resources.objects.all()
    context = {
        'courses': courses,
    }
    return render(request , 'main/resources.html' , context)

def topStartUps(request):
    startups = StartUps.objects.all()
    context = {
        'startups': startups,
    }
    return render(request , 'main/startups.html' , context)

def prediction(request):
    return render(request , 'main/Startup-Success-Prediction-using-ML.html')
