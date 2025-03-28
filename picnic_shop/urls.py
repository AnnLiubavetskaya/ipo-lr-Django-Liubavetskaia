from django.urls import path
from .views import author
from .views import shop
from .views import main

urlpatterns = [
    path('main/author.html', author, name='author'),
    path('main/shop.html',shop, name = 'shop' ),
    path('main/',main, name = 'main' ),
]