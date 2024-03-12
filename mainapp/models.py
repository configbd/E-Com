from django.db import models
from django.urls import reverse
from prose.fields import RichTextField


# Create your models here.
class Slider(models.Model):
    name=models.CharField(max_length=30)
    slider_image = models.ImageField(upload_to='slider_images/')
    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    price = models.FloatField(verbose_name='Regular Price')
    discount_price = models.FloatField(verbose_name='Discounted Price')
    item_image = models.ImageField(upload_to='items_images/')
    description =  RichTextField(blank=True, null=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('mainapp:product_details', kwargs={
            'pk': self.pk
        })
    def discount_percentage(self):
        return round((((self.price - self.discount_price) / self.price) * 100),2)


    @staticmethod
    def get_items_by_id(ids):
        return Item.objects.filter(id__in =ids)
    
class HotDealsProduct(models.Model):
    hot_item=models.ManyToManyField(Item)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"'{self.item.item_name}': [ {self.item.discount_price} x {self.quantity}ps={self.item.discount_price * self.quantity} TK ]"
    def subtotal(self):
        return self.item.discount_price * self.quantity

class ItemOrder(models.Model):
    ordered_items = models.ManyToManyField(CartItem)
    customer_name=models.CharField(max_length=20,blank=True, null=True)
    phone_number=models.CharField(max_length=11,blank=True, null=True)
    shipping_address = models.CharField(max_length=20, blank=True, null=True)
    shipping_cost= models.PositiveSmallIntegerField(blank=True, null=True)
    # shipping_area=models.TextField(max_length=100,blank=True, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_ordered_confirm = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    def __str__(self):
        return self.customer_name
    def total_price(self):
        total = sum(cart_item.subtotal() for cart_item in self.ordered_items.all())
        return f"{total+self.shipping_cost} TK"
    
    class Meta:
        ordering = ["-ordered_date"]

