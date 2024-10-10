from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
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



def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(Cartitem, product=product, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    
    return redirect('cart:cart')


def increase_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    selected_size = request.POST.get('size', 'M')
    
    # Get or create the cart for the user
    
    # Get or create the CartItem for the product in the user's cart
    cart_item, created = Cartitem.objects.get_or_create(user=request.user, product=product,size=selected_size)
    
    # Increase the quantity of the cart item
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart')  # Redirect to the cart page

def decrease_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item = get_object_or_404(Cartitem, product=product, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Optionally, remove the item if quantity reaches 0
    return redirect('cart:cart')