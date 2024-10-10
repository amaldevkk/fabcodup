from django.shortcuts import render,get_object_or_404 ,redirect
from django.db.models import Q

from .models import Product
from cart. models import Cartitem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):

    products = Product.objects.all()
    page = request.GET.get('page', 1)

    product_paginator = Paginator(products,4)
    
    try:

        products = product_paginator.page(int(page))
    except  PageNotAnInteger:
        products = Paginator.page(1)
    except EmptyPage: 
        products = Paginator.page(Paginator.num_pages)

    return render(request,'index.html', {'products' : products} )


def shop(request,):
    

    products = Product.objects.all()

        #filter price 

    price_ranges = request.GET.getlist('price_range')
    if price_ranges:
        price_query = Q()  # Initialize an empty Q object
        for range_str in price_ranges:
            if '-' in range_str:
             
             min_price, max_price = map(int, range_str.split('-'))  # Parse min and max price
             price_query |= Q(price__gte=min_price, price__lte=max_price)  # Build the query
            elif range_str =="10000-":
                price_query |= Q(price__gte=10000)  
        products = products.filter(price_query)

    colors = request.GET.getlist('color')
    if colors:
        color_query = Q()  # Initialize an empty Q object
        
        # If "All Color" is not selected, filter by selected colors
        if "all" not in colors:
            for color in colors:
                color_query |= Q(color=color)  # Assuming you have a field `color` in your Product model

            products = products.filter(color_query)

    # search filter
    query = request.GET.get('q')
    

    if query:
        products = products.filter(name__icontains='query')


     # Sorting functionality
    sort_by = request.GET.get('sort')  # Get the sort option from the request
    if sort_by == 'latest':
        products = products.order_by('-created_at')  # Assuming you have a created_at field
    elif sort_by == 'popularity':
        products = products.order_by('-popularity')  # Assuming you have a popularity field
    elif sort_by == 'best_rating':
        products = products.order_by('-rating')  # Assuming you have a rating field





    #paginator
    page = request.GET.get('page', 1)

    product_paginator = Paginator(products,3)
    
    try:

        products = product_paginator.page(int(page))
    except  PageNotAnInteger:
        products = Paginator.page(2)
    except EmptyPage: 
        products = Paginator.page(Paginator.num_pages)
   


    context = {
        'products': products,
        'price_ranges': price_ranges,
        'query' : query,

    }
        

    return render(request, 'shop.html', context)




def detail(request):
    return render(request,'detail.html')


def contact(request):
    return render(request, 'contact.html')

def itemproducts(request,):
    products = Product.objects.all()


    return render(request, 'item_products.html', {'products' : products} )

def productviews(request,category,):
    products = Product.objects.all()

    query = request.GET.get('q')
    
    if category: 
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()  # Display all products if no category selected

    if query:
        products = products.filter(name__icontains='query')

    price_range = request.GET.getlist('price_range')
    if price_range:
        pass

    context = {
        'products': products,
        'query': query
    }

    return render(request,'productview.html', context)


def productsdetails(request,pk):

    product = get_object_or_404(Product, pk=pk)

   
    return render(request, 'products_items_details.html', {'product' : product})



