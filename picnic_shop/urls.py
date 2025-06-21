from django.urls import path
from .views import author
from .views import shop
from .views import main
from . import views

urlpatterns = [
    path('main/author.html', author, name='author'),
    path('main/shop.html',shop, name = 'shop' ),
    path('main/',main, name = 'main' ),
    #15 lr
    path('spec/', views.qualifications_list, name='qualifications_list'),
    path('spec/<int:id>/', views.qualification_detail, name='qualification_detail'),
    #17lr
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
]