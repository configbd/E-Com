from django.urls import path

from .views import (HomeView,ItemDetailView,add_to_cart,checkout_page,CheckOut)

app_name = 'mainapp'

urlpatterns = [
     path('',HomeView.as_view(), name='home_page'),
     path('item_list/<category_name>',HomeView.as_view(), name='item_list_by_category'),
     path('product-details/?p=<int:pk>',ItemDetailView.as_view(), name='product_details'),
     path('add_to_cart',add_to_cart, name='add_to_cart'),
     path('checkout_page/',checkout_page, name='checkout_page'),
     path('order_confirm/', CheckOut.as_view(), name='order_confirm')
     
]