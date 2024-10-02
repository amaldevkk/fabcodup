from . import  views 
from django.urls import path
from django.conf.urls.static import static



urlpatterns = [
      path('', views.index, name='index' ),

      path ('shop/', views.shop, name='shop'),

      path ('detail/', views.detail, name='detail'),

      path ('contact/', views.contact, name='contact'),

      path ('produtcs/', views.itemproducts, name='product'),

      path ('produtcview/<str:category>/', views.productviews, name='productview'),

      path ('productdetls/<int:pk>/', views.productsdetails, name='productsdetils'),

    
]
