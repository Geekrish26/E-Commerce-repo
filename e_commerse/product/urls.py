from django.urls import path
from .views import *
app_name = "product"
urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('product-detail/<slug:pk>/', ItemDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('index/', HomeView.as_view(), name='index')
]

