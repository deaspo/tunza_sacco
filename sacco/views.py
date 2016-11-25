from django.shortcuts import render
from sacco.models import Product

# Create your views here.
product = Product.objects.all()

def index(request):
    return render(request, 'home/index.html',{'products':product})

def products(request):
    return render(request, 'products/products.html',{'products':product})

def about(request):
    return render(request, 'about.html')

def membership(request):
    return render(request, 'membership/membership.html')