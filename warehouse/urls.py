from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products.as_view()),
    path('cart/', views.carts.as_view()),
    path('order/', views.placeOrder.as_view()),
    path('viewproduct/', views.viewProduct.as_view())
]