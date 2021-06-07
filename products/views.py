'''
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
'''

from django.shortcuts import render

from products.models import Product, ProductCategory

# Create your views here.
# функции = контроллер = вьюхи = представления
def index(request):
    context = {
        'title' : 'GeekShop',
    }
    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title': 'GeekShop Products',
        # 'categories': [
        #     'Новинки',
        #     'Одежда',
        #     'Обувь',
        #     'Аксессуары',
        #     'Подарки',
        # ],

    }
    context['products'] = Product.objects.all()
    print(Product.objects.all())


    context['categories'] = ProductCategory.objects.all()
    # print(ProductCategory.objects.all())
    # print(ProductCategory.objects.get(id=1))

    return render(request, 'products/products.html', context)
