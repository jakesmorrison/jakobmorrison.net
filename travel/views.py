from django.shortcuts import render
from .models import CreditCard, User, Issued

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'travel/home2.html', context)