import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project_2.settings') 
import django
django.setup()

from picnic_shop.models import Manufacturer, Category, Product, Cart, CartItem
from django.contrib.auth.models import User
from django.core.files import File
import random

# Очистка базы (опционально)
Manufacturer.objects.all().delete()
Category.objects.all().delete()
Product.objects.all().delete()
User.objects.all().delete()

# 1. 5 производителей
manufacturers = [
    {"name": "PicnicPro", "country": "Германия", "description": "Немецкое качество для отдыха"},
    {"name": "GrillMaster", "country": "Россия", "description": "Лучшие мангалы и аксессуары"},
    {"name": "OutdoorGear", "country": "США", "description": "Снаряжение для активного отдыха"},
    {"name": "NatureLover", "country": "Франция", "description": "Экологичные товары для пикника"},
    {"name": "Campy", "country": "Италия", "description": "Стильные аксессуары для кемпинга"},
]
for m in manufacturers:
    Manufacturer.objects.create(**m)
print(" Производители добавлены (5 шт.)")

# 2. 10 категорий
categories = [
    {"name": "Мангалы и грили", "description": "Угольные, газовые и электрические грили"},
    {"name": "Посуда для пикника", "description": "Тарелки, стаканы, столовые приборы"},
    {"name": "Термосы и термокружки", "description": "Для горячих и холодных напитков"},
    {"name": "Пледы и коврики", "description": "Для комфортного отдыха на природе"},
    {"name": "Сумки-холодильники", "description": "Переносные холодильники для еды"},
    {"name": "Наборы для пикника", "description": "Готовые комплекты для отдыха"},
    {"name": "Шампуры и аксессуары", "description": "Для приготовления мяса на огне"},
    {"name": "Складная мебель", "description": "Стулья, столы и шезлонги"},
    {"name": "Освещение", "description": "Фонари, лампы и гирлянды"},
    {"name": "Игры и развлечения", "description": "Мячи, бадминтон, настольные игры"},
]
for cat in categories:
    Category.objects.create(**cat)
print(" Категории добавлены (10 шт.)")

# 3. 34 товара
products_data = [
    # Мангалы и грили (5 товаров)
    {"name": "Мангал складной 'Compact'", "description": "Компактный для путешествий", "price": 1999, "stock": 15},
    {"name": "Гриль газовый 'Premium'", "description": "3 конфорки, мощность 2.5 кВт", "price": 8999, "stock": 8},
    {"name": "Мангал 'Огонёк'", "description": "Классический стальной", "price": 1499, "stock": 20},
    {"name": "Гриль электрический 'Mini'", "description": "Для балкона и дачи", "price": 3499, "stock": 12},
    {"name": "Коптильня 'Дымок'", "description": "Для холодного копчения", "price": 2599, "stock": 5},
    
    # Посуда (5 товаров)
    {"name": "Набор посуды 'Picnic Set'", "description": "12 предметов, нержавеющая сталь", "price": 1499, "stock": 30},
    {"name": "Термокружка 'Travel'", "description": "Сохраняет тепло 6 часов", "price": 799, "stock": 40},
    {"name": "Набор пластиковых стаканов", "description": "6 шт., небьющиеся", "price": 299, "stock": 50},
    {"name": "Складная кастрюля", "description": "Экономит место в рюкзаке", "price": 1299, "stock": 15},
    {"name": "Набор столовых приборов", "description": "Нержавеющая сталь, 4 предмета", "price": 599, "stock": 25},
    
    # Термосы (3 товара)
    {"name": "Термос 1л 'Standard'", "description": "Сохраняет тепло 12 часов", "price": 1200, "stock": 20},
    {"name": "Термос 0.5л 'Compact'", "description": "Удобный для прогулок", "price": 899, "stock": 30},
    {"name": "Термос 2л 'Family'", "description": "Для большой компании", "price": 1799, "stock": 10},
    
    # Пледы (3 товара)
    {"name": "Плед 'Уют'", "description": "Шерстяной, размер 150x200 см", "price": 899, "stock": 18},
    {"name": "Коврик туристический", "description": "Водонепроницаемый", "price": 499, "stock": 25},
    {"name": "Плед 'Picnic'", "description": "Легкий, с водоотталкивающей пропиткой", "price": 699, "stock": 15},
    
    # Сумки-холодильники (3 товара)
    {"name": "Сумка-холодильник 20л", "description": "Для семьи из 4 человек", "price": 1999, "stock": 10},
    {"name": "Сумка-холодильник 10л", "description": "Компактная для двоих", "price": 1299, "stock": 15},
    {"name": "Термопакет 'Lunch'", "description": "Для перекуса на работе", "price": 499, "stock": 30},
    
    # Наборы для пикника (3 товара)
    {"name": "Набор 'Basic'", "description": "Мангал + шампуры + угли", "price": 2499, "stock": 8},
    {"name": "Набор 'Premium'", "description": "Все для идеального пикника", "price": 5999, "stock": 5},
    {"name": "Набор 'Romantic'", "description": "Для пикника вдвоем", "price": 3499, "stock": 7},
    
    # Шампуры (3 товара)
    {"name": "Шампуры стальные", "description": "Набор из 6 шт.", "price": 399, "stock": 40},
    {"name": "Шампуры складные", "description": "Удобны для транспортировки", "price": 599, "stock": 25},
    {"name": "Шампуры 'Гриль'", "description": "С деревянными ручками", "price": 499, "stock": 30},
    
    # Складная мебель (3 товара)
    {"name": "Стул складной", "description": "Выдерживает до 120 кг", "price": 999, "stock": 20},
    {"name": "Стол походный", "description": "Раскладной, вес 2 кг", "price": 1499, "stock": 15},
    {"name": "Шезлонг складной", "description": "С регулируемой спинкой", "price": 1999, "stock": 10},
    
    # Освещение (3 товара)
    {"name": "Фонарь LED", "description": "Яркость 300 люмен", "price": 699, "stock": 25},
    {"name": "Гирлянда солнечная", "description": "Автоматическое включение", "price": 499, "stock": 30},
    {"name": "Свечи декоративные", "description": "Набор из 12 шт.", "price": 299, "stock": 40},
    
    # Игры (3 товара)
    {"name": "Бадминтон", "description": "2 ракетки + 3 волана", "price": 799, "stock": 20},
    {"name": "Настольная игра 'Picnic'", "description": "Для компании до 6 человек", "price": 1299, "stock": 15},
    {"name": "Мяч волейбольный", "description": "Для пляжа и лужаек", "price": 899, "stock": 12},
]

manufacturers = list(Manufacturer.objects.all())
categories = list(Category.objects.all())

for i, data in enumerate(products_data):
    # Распределяем товары по категориям и производителям
    category = categories[i % len(categories)]
    manufacturer = manufacturers[i % len(manufacturers)]
    
    Product.objects.create(
        **data,
        category=category,
        manufacturer=manufacturer,
        # photo=File(open(f'media/products/{i+1}.jpg', 'rb'))  # Раскомментируйте если есть изображения
    )
print(" Товары добавлены (34 шт.)")

# 4. 5 пользователей с корзинами
users_data = [
    {"username": "alex", "email": "alex@mail.com", "password": "picnic123"},
    {"username": "olga", "email": "olga@mail.com", "password": "olga2024"},
    {"username": "ivan", "email": "ivan@mail.com", "password": "ivan_picnic"},
    {"username": "anna", "email": "anna@mail.com", "password": "anna_camp"},
    {"username": "max", "email": "max@mail.com", "password": "max_outdoor"},
]

products = list(Product.objects.all())

for user_data in users_data:
    user = User.objects.create_user(**user_data)
    cart = Cart.objects.create(user=user)
    
    # Добавляем 2 случайных товара в корзину
    for product in random.sample(products, 2):
        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=random.randint(1, 3)  # Случайное количество от 1 до 3
        )
print(" Пользователи и корзины созданы (5 пользователей)")

print(" Все данные успешно добавлены в базу!")