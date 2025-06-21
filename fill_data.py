import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project_2.settings') 
import django
django.setup()

from picnic_shop.models import Manufacturer, Category, Product, Cart, CartItem
from django.contrib.auth.models import User

# Очистка базы (опционально)
Manufacturer.objects.all().delete()
Category.objects.all().delete()
Product.objects.all().delete()
User.objects.all().delete()

# 1. 5 производителей
manufacturers = [
    {"name": "PicnicPro", "country": "Германия", "description": "Немецкое качество"},
    {"name": "GrillMaster", "country": "Россия", "description": "Мангалы и грили"},
    {"name": "OutdoorGear", "country": "США", "description": "Для активного отдыха"},
    {"name": "NatureLover", "country": "Франция", "description": "Эко-товары"},
    {"name": "Campy", "country": "Италия", "description": "Стильные аксессуары"},
]
for m in manufacturers:
    Manufacturer.objects.create(**m)

# 2. 10 категорий
categories = [
    {"name": "Мангалы и грили", "description": "Для шашлыка"},
    {"name": "Посуда", "description": "Тарелки, стаканы"},
    {"name": "Термосы", "description": "Для напитков"},
    {"name": "Пледы", "description": "Для комфорта"},
    {"name": "Сумки-холодильники", "description": "Для еды"},
    {"name": "Наборы для пикника", "description": "Готовые комплекты"},
    {"name": "Шампуры", "description": "Для мяса"},
    {"name": "Складная мебель", "description": "Стулья, столы"},
    {"name": "Освещение", "description": "Фонари"},
    {"name": "Игры", "description": "Для развлечений"},
]
for cat in categories:
    Category.objects.create(**cat)

# 3. 3 товара 
grill = Product.objects.create(
    name="Мангал 'Огонёк'",
    description="Компактный складной",
    price=1999,
    stock=15,
    category=Category.objects.get(name="Мангалы и грили"),
    manufacturer=Manufacturer.objects.get(name="GrillMaster"),
)

thermos = Product.objects.create(
    name="Термос 1л",
    description="Сохраняет тепло 12 часов",
    price=1200,
    stock=20,
    category=Category.objects.get(name="Термосы"),
    manufacturer=Manufacturer.objects.get(name="NatureLover"),
)

blanket = Product.objects.create(
    name="Плед 'Уют'",
    description="Размер 150x200 см",
    price=899,
    stock=10,
    category=Category.objects.get(name="Пледы"),
    manufacturer=Manufacturer.objects.get(name="Campy"),
)

# 4. 2 пользователя с корзинами
users = [
    {"username": "alex", "email": "alex@mail.com", "password": "picnic123"},
    {"username": "olga", "email": "olga@mail.com", "password": "olga2024"},
]
for user_data in users:
    user = User.objects.create_user(**user_data)
    cart = Cart.objects.create(user=user)
    # Добавляем товары в корзину
    CartItem.objects.create(cart=cart, product=grill, quantity=1)
    CartItem.objects.create(cart=cart, product=thermos, quantity=2)

print("✅ Данные успешно добавлены!")