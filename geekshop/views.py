from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket


def index(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'главная'
    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }

    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'

    context = {
        'title': title,
    }

    return render(request, 'geekshop/contact.html', context=context)
