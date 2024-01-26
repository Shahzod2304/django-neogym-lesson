from urllib import request
from django.shortcuts import render

# Create your views here.
def Main(request):
    context = {
        'active_page':'main',
    }
    
    return render(request, 'index.html', context)

def Contact(request):
    context = {
        'active_page':'contact',
    }

    return render(request, 'contact.html', context)

def Trainer(request):
    context = {
        'active_page':'trainer',
    }

    return render(request, 'trainer.html', context)

def Why(request):
    context = {
        'active_page':'why',
    }

    return render(request, 'why.html', context)