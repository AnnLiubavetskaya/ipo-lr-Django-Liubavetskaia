from django.contrib import admin

# Register your models here.

from .models import Manufacturer, Category, Product, Cart, CartItem

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
