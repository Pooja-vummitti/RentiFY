from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),

    path('services',views.servicepage, name="servicepage"),

    path('about',views.aboutuspage, name="aboutuspage"),

    path('accounts/signup', views.signup, name="signup"),
    
    path('product', views.product, name="products"),

    

    path('renting', views.renting, name = "renting"),

    path('cart', views.cart, name = "cart"),

    path('checkout', views.checkout, name = "checkout"),

    path('pricing', views.pricing, name = "pricing"),

    path('contact', views.contact, name = "contact"),

    path('updateItem', views.updateItem, name = "updateItem"),

    path('products_HW', views.products_HW, name = "products_HW"),

    path('products_SW', views.products_SW, name = "products_SW")
]
