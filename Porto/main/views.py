from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    cats = Category.objects.all()
    products = Products.objects.all()
    subcats = SubCategory.objects.all()
    return render(request, 'main/index.html', {'cats': cats, 'products': products, 'subcats': subcats})


def show_cat(request, cat_id):
    prods = Products.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    return render(request, 'main/category.html', {'prods': prods, 'cats': cats})


def show_subcat(request, subcat_id):
    prods = Products.objects.filter(subcat_id=subcat_id)
    cats = Category.objects.all()
    return render(request, 'main/category.html', {'prods': prods, 'cats': cats})


def show_product(request, prod_id):
    prod = Products.objects.filter(pk=prod_id)
    return render(request, 'main/product.html', {'prod': prod})


def show_all(request):
    products = Products.objects.all()
    return render(request, 'main/all_categories.html', {'products': products})
