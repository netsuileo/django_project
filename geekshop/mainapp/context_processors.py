def menu_links(request):
    return {
        "menu": {
            "index": "Главная",
            "products": "Продукты",
            "contact": "Контакты",
        }
    }


def basket(request):
    return {"basket": getattr(request.user, "basket", None)}
