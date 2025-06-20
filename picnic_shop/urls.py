from django.urls import path
from .views import author
from .views import shop
from .views import main
from . import views

urlpatterns = [
    path('main/author.html', author, name='author'),
    path('main/shop.html',shop, name = 'shop' ),
    path('main/',main, name = 'main' ),
    path('spec/', views.qualifications_list, name='qualifications_list'),
    path('spec/<int:id>/', views.qualification_detail, name='qualification_detail'),
]