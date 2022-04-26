from django.shortcuts import render

from .models import Category, Product

MENU_LINKS = {
    "index": "Главная",
    "products": "Продукты",
    "contact": "Контакты",
}


def index(request):
    return render(
        request,
        "mainapp/index.html",
        context={
            "title": "Главная",
            "menu": MENU_LINKS,
        },
    )


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:3]
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu": MENU_LINKS,
            "products": products,
            "categories": categories,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "menu": MENU_LINKS,
        },
    )
