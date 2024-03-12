from django import forms
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import (Item, 
                     Category,
                     Slider,
                     CartItem,
                     HotDealsProduct,
                     ItemOrder
                     )


class PostAdminForm(forms.ModelForm):
    

    class Meta:
        model = Item
        fields = '__all__'

@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    list_display=['item_name','item_category','price','discount_price','display_image']
    form = PostAdminForm
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.item_image.url}" width="60" height="60" />')

    display_image.short_description = 'Item Image'



@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone_number','shipping_address', 'ordered_date','shipping_area','display_cart_items','total_price','is_ordered_confirm_display']
    def display_cart_items(self, obj):
        cart_items = obj.ordered_items.all()
        return format_html_join('\n', '<li>{}</li>', ((str(cart_item),) for cart_item in cart_items))

    display_cart_items.short_description = "Ordered Items"
    def shipping_area(self,obj):
        shipping_cost=obj.shipping_cost
        return f'Inside Dhaka ({shipping_cost} TK)' if shipping_cost==60 else f"Outside Dhaka ({shipping_cost} TK)"
    
    def is_ordered_confirm_display(self, obj):
        return obj.is_ordered_confirm

    is_ordered_confirm_display.boolean = True
    is_ordered_confirm_display.short_description = 'Confirmation'

    actions = ['mark_ordered_confirm','mark_ordered_unconfirm']

    def mark_ordered_confirm(self, request, queryset):
        queryset.update(is_ordered_confirm=True)
    def mark_ordered_unconfirm(self, request, queryset):
        queryset.update(is_ordered_confirm=False)
    mark_ordered_confirm.short_description = "Confirm selected Order"
    mark_ordered_unconfirm.short_description = "Unonfirm selected Order"

@receiver(post_delete, sender=ItemOrder)
def delete_unassociated_cart_items(sender, instance, **kwargs):
    # Retrieve all CartItem instances that are not associated with any ItemOrder
    unassociated_cart_items = CartItem.objects.filter(itemorder=None)
    # Delete the unassociated CartItem instances
    unassociated_cart_items.delete()

# admin.site.register(Item) 
admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(HotDealsProduct)
