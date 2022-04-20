from django.shortcuts import render

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
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "menu": MENU_LINKS,
            "products": [
                {
                    "name": "Стул 1",
                    "description": "отличный стул!",
                    "image": "img/product-11.jpg",
                },
                {
                    "name": "Стул 2",
                    "description": "отличный стул 2!",
                    "image": "img/product-21.jpg",
                },
                {
                    "name": "Стул 3",
                    "description": "отличный стул 3!",
                    "image": "img/product-31.jpg",
                },
            ],
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
