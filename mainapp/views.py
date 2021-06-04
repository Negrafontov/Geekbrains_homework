from django.shortcuts import render
from .models import Product


def products(request, pk=None):
    title = 'продукты'

    if pk:
        product = Product.objects.get(pk=pk)
        context = {
            'product': product,
        }
        return render(request, 'mainapp/product.html', context=context)

    links_menu = [
        {'href': 'mainapp:products', 'name': 'все'},
        {'href': 'mainapp:products', 'name': 'дом'},
        {'href': 'mainapp:products', 'name': 'офис'},
        {'href': 'mainapp:products', 'name': 'модерн'},
        {'href': 'mainapp:products', 'name': 'классика'},
    ]

    context = {
        'links_menu': links_menu,
        'title': title,
    }

    return render(request, 'mainapp/products.html', context=context)
