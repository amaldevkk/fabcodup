from django.shortcuts import render,redirect
from products.models import Product
from cart .models import Cartitem


# Create your views here.
##def cart(request):
  #  cart_items = Cartitem.objects.filter(user=request.user)
  #  total_price = sum(item.product.price * item.quantity for item in cart_items)
  #  return render(request, 'caart/cart.html', {'cart_items': cart_items, 'total_price': total_price})



  

    # Or, to get all items in the cart
    

def cart(request):
    cart_items = Cartitem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'caart/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cartitem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart')



def remove_from_cart(request, item_id):
    cart_item = Cartitem.objects.get(id=item_id)
    cart_item.delete()
    return redirect(request,'cart:cart')