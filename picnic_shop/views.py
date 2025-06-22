
from django.shortcuts import render
from django.http import Http404
import json
import os
import logging
from django.conf import settings

#17
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Cart, CartItem

# Настройка логгера
logger = logging.getLogger(__name__)

def load_qualifications():
    """Загрузка и фильтрация данных"""
    try:
        with open('picnic_shop/dump.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        processed_data = []
        for item in data:
            if isinstance(item, dict) and 'pk' in item and 'fields' in item:
                # Преобразуем только числовые ID
                if isinstance(item['pk'], int) or str(item['pk']).isdigit():
                    new_item = {'id': int(item['pk'])}
                    new_item.update(item['fields'])
                    processed_data.append(new_item)
        
        return processed_data
        
    except Exception as e:
        logger.error(f"Ошибка загрузки: {str(e)}")
        raise

def qualifications_list(request):
    """Только валидные данные"""
    try:
        qualifications = [
            q for q in load_qualifications()
            if isinstance(q.get('id'), int)  # Гарантируем числовой ID
        ]
        return render(request, 'qualifications_list.html', {
            'qualifications': qualifications,
            'error': None if qualifications else "Нет корректных данных"
        })
    except Exception as e:
        return render(request, 'qualifications_list.html', {
            'qualifications': [],
            'error': "Ошибка загрузки"
        })

def qualification_detail(request, id):
    """Детали одного учреждения"""
    try:
        qualifications = load_qualifications()
        qualification = next((q for q in qualifications if q['id'] == int(id)), None)
        
        if not qualification:
            logger.warning(f"Учреждение с id={id} не найдено")
            raise Http404("Учреждение не найдено")
            
        return render(request, 'qualification_detail.html', {
            'qualification': qualification
        })
    except Exception as e:
        logger.error(f"Ошибка в qualification_detail: {str(e)}")
        raise Http404("Произошла ошибка")

def author(request):
    return render(request, 'author.html');

def shop(request):
    return render(request, 'shop.html');

def main(request):
    return render(request, 'main.html');

#17lr

def product_list(request):
    products = Product.objects.all()
    
    # Фильтрация по категории и производителю
    category = request.GET.get('category')
    manufacturer = request.GET.get('manufacturer')
    
    if category:
        products = products.filter(category__name=category)
    if manufacturer:
        products = products.filter(manufacturer__name=manufacturer)
    
    # Поиск по названию и описанию
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
    
    return redirect('cart_view')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    new_quantity = int(request.POST.get('quantity', 1))
    
    if 0 < new_quantity <= cart_item.product.stock:
        cart_item.quantity = new_quantity
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cart_items.all()
    total_price = sum(item.item_price() for item in cart_items)
    
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
