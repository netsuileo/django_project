import datetime

from django import template

register = template.Library()


@register.simple_tag
def current_year():
    return datetime.datetime.now().year


@register.simple_tag
def disabled_if_cannot_buy(user, product):
    if user.is_anonymous:
        return 'disabled'

    if product.quantity == 0:
        return 'disabled'

    basket_item = user.basket.filter(product=product).first()    
    if basket_item and basket_item.quantity + 1 > product.quantity:
        return 'disabled'

    return ''
