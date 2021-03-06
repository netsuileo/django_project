from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from mainapp.models import Product

from .models import Basket


@login_required
def view(request):
    return render(request, "basketapp/view.html", context={"title": "Корзина"})


@login_required
def add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    if basket:
        basket_item = basket[0]
        basket_item.quantity += 1
    else:
        basket_item = Basket(user=request.user, product=product)

    if basket_item.quantity <= product.quantity:
        basket_item.save()

    if "next" in request.META.get("HTTP_REFERER"):
        redirect_url = reverse("index")
    else:
        redirect_url = request.META.get("HTTP_REFERER", reverse("index"))    

    return HttpResponseRedirect(redirect_url)


@login_required
def remove(request, basket_id):
    basket = get_object_or_404(Basket, pk=basket_id)
    basket.quantity -= 1
    if not basket.quantity:
        basket.delete()
    else:
        basket.save()
    return HttpResponseRedirect(reverse("basket:view"))


@login_required
def edit(request, basket_id, quantity):
    basket = get_object_or_404(Basket, pk=basket_id)
    basket.quantity = quantity
    if not basket.quantity:
        basket.delete()
    else:
        basket.save()
    return render(request, "basketapp/includes/inc_basket_list.html")
