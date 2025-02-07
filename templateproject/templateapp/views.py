from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def templateview(request):
    return render(request, 'templateapp/home.html')


def electronicview(request):
    return render(request, 'templateapp/electronics.html')


def shoesview(request):
    return render(request, 'templateapp/shoes.html')


def clothingview(request):
    return render(request, 'templateapp/clothing.html')
