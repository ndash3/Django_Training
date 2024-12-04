from django.shortcuts import render

# Create your views here.


def templateview(request):
    return render(request, 'templateapp/home.html')


def electronicview(request):
    return render(request, 'templateapp/electronics.html')

def shoesview(request):
    return render(request, 'templateapp/shoes.html')


def clothingview(request):
    return render(request, 'templateapp/clothing.html')
