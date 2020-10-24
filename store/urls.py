from django.urls import path 
from . import views 

urlpatterns = [
    #leave path as empty string for url 
    path('', views.store, name ="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]