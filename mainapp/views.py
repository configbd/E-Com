from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.db.models import Q
# Create your views here.
from .models import (ItemOrder,Item,CartItem)

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"
    paginate_by = 8
    ordering = '-id'

    def get_queryset(self):
        queryset = Item.objects.all()
        category = self.kwargs.get('category_name')
        search_by = self.request.GET.get('key')
        cat_name = self.request.GET.get('cat_name')
        # Return queryset filtered by the category
        if category:
            queryset = queryset.filter(item_category__category=category)
        if search_by:
            queryset = queryset.filter(
                Q(item_category__category__icontains=search_by) |
                Q(item_name__icontains=search_by)
            )
        if cat_name:
            queryset = queryset.filter(
                Q(item_category__category__icontains=cat_name) &
                Q(item_name__icontains=search_by)
            )
        return queryset.order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        messages_data = messages.get_messages(self.request)
        return context
    
class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

 

def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        remove = request.POST.get('remove')
        delete = request.POST.get('delete')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(item_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(item_id)
                    else:
                        cart[item_id]  = quantity-1
                else:
                    cart[item_id]  = quantity+1

            else:
                cart[item_id] = 1
        else:
            cart = {}
            cart[item_id] = 1

        if delete:
            cart.pop(item_id)

        request.session['cart'] = cart
        request.session.modified = True
        return redirect('mainapp:checkout_page')
    return redirect('mainapp:home_page')




def checkout_page(request):
    cart = request.session.get('cart')
    total=0
    for key ,val in cart.items():
        total+=float(Item.objects.get(id=key).price*float(val))
    keys = cart.keys()
    ids_list = [int(id) for id in keys]
    item_list = Item.objects.filter(id__in=ids_list)


    return render(request,'checkout.html',{'item_list':item_list,'subtotal':total})
from django.views import View


class CheckOut(View):
    def post(self, request):
        customer_name = request.POST.get('customer_name')
        phone_number = request.POST.get('phone_number')
        shipping_cost = request.POST.get('shipping_cost')
        shipping_address = request.POST.get('shipping_address')
        cart = request.session.get('cart')
        new_order=ItemOrder.objects.create(customer_name=customer_name,phone_number=phone_number,shipping_cost=shipping_cost,shipping_address=shipping_address)
        for key ,val in cart.items():
            objects_list=CartItem.objects.create(item=Item.objects.get(id=key),quantity=val)
            new_order.ordered_items.add(objects_list)
        request.session['cart'] = {}
        messages.success(request, 'Form submitted successfully!')

        return redirect('mainapp:home_page')