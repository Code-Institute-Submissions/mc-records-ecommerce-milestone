from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    """Allows user to search for products"""
    products = Product.objects.filter(artist__icontains = request.GET['q']) | Product.objects.filter(album__icontains = request.GET['q'])
    return render(request, 'products.html', {"products": products})

