from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    context={
    }
    return render(request,"finance/home.html",context)

def investment_analyzer(request):
    context={
    }
    return render(request,"finance/investment_analyzer_1.html",context)


def retirement_withdrawl(request):
    context={
    }
    return render(request,"finance/retirement_withdrawl.html",context)