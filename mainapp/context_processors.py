from .models import Category,HotDealsProduct,Slider
def header_data(request):
    # request.session.clear()
    cart = request.session.get('cart')
    if cart==None :
        request.session['cart'] = {}
        request.session.modified = True
        cart_length = 0
    else:
        cart_length =len(cart)
    hot_deals_product = HotDealsProduct.objects.all()[0].hot_item.all()
    categories = Category.objects.all()
    sliders = Slider.objects.all()

    return {'cart_length': cart_length,'categories':categories,'hot_deals_product':hot_deals_product,'sliders':sliders}

