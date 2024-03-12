# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='check_item_id')
def check_item_id(cart, item_id):
    found_item = False
    for item in cart:
        if item.get('item_id') == item_id:
            found_item = True
            break
    return found_item
