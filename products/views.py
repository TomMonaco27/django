'''
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
'''

from django.shortcuts import render

from products.models import Product, ProductCategory

def index(request):
    context = {
        'title' : 'GeekShop',
    }
    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title': 'GeekShop Products',
    }
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'products/products.html', context)
