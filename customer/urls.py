from django.urls import path

from . import views

urlpatterns = [
    path('home', views.customer, name='customer'),
    path('cart',views.cart, name='cart'),
    path('',views.signin, name='signin')
]