from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(items  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == items.id:
            return True
    return False

@register.filter(name='card_quantity')
def card_quantity(items,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == items.id:
            return cart.get(id)
    return 0


@register.filter(name='item_total')
def item_total(items,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == items.id:
            return float(cart.get(id))*float(items.price)
    return 0
