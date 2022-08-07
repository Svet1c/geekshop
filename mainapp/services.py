from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user):
    basket_list = []
    if user.is_authenticated:
        basket_list = Basket.objects.filter(user=user)

    return basket_list


def get_hot_product():
    return Product.objects.all().order_by('?').first()


def get_same_products(prod):
    return Product.objects.filter(category=prod.category).exclude(pk=prod.pk)[:3]
