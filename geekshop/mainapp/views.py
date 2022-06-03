import random

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Category, Product


def index(request):
    return render(
        request,
        "mainapp/index.html",
        context={"title": "Главная"},
    )


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    hot_product = random.choice(products)
    products = products.exclude(pk=hot_product.pk)[:3]
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "hot_product": hot_product,
            "products": products,
            "categories": categories,
        },
    )


def product(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)
    return render(
        request,
        "mainapp/product.html",
        context={
            "title": product.name,
            "product": product,
            "category": product.category,
            "categories": categories,
        },
    )


def category(request, pk, page=1):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category).order_by("price")
    paginator = Paginator(products, per_page=3)

    if page > paginator.num_pages:
        return HttpResponseRedirect(reverse("category", args=[category.id]))

    return render(
        request,
        "mainapp/category.html",
        context={
            "title": "Продукты",
            "products": paginator.page(page),
            "category": category,
            "categories": categories,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
        },
    )
