from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product, Category
from mainapp.services import get_basket, get_hot_product, get_same_products


def index(request):
    context = {
        'products': Product.objects.all()[:4],
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = Category.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(Category, pk=pk)
            products_list = Product.objects.filter(category_id=pk)
        context = {
            'links_menu': links_menu,
            'products': products_list,
            'category': category_item,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/products_list.html', context)
    hot_prod = get_hot_product()
    same_prod = get_same_products(hot_prod)
    context = {
        'links_menu': links_menu,
        'basket': get_basket(request.user),
        'hot_product': hot_prod,
        'same_products': same_prod
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    links_menu = Category.objects.all() 
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'product': product_item,
        'basket': get_basket(request.user),
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/product.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context)