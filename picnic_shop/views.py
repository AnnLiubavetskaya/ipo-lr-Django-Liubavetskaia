from django.shortcuts import render
import json
from django.http import Http404
import os
import logging
from django.conf import settings

# Инициализация логгера
logger = logging.getLogger(__name__)
# Загрузка данных из JSON
def load_qualifications():
    """Загрузка данных из JSON с новой структурой"""
    try:
        json_path = os.path.join(settings.BASE_DIR, 'picnic_shop', 'dump.json')
        
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Преобразование структуры данных
        processed_data = []
        for item in data:
            if isinstance(item, dict) and 'pk' in item and 'fields' in item:
                new_item = {'id': item['pk']}
                new_item.update(item['fields'])
                processed_data.append(new_item)
        
        return processed_data
        
    except Exception as e:
        logger.error(f"Ошибка загрузки JSON: {str(e)}", exc_info=True)
        raise

# Список всех квалификаций
def qualifications_list(request):
    """Список всех квалификаций"""
    try:
        qualifications = load_qualifications()
        return render(request, 'qualifications_list.html', {
            'qualifications': qualifications
        })
    except Exception as e:
        logger.error(f"Ошибка в qualifications_list: {str(e)}", exc_info=True)
        raise Http404("Не удалось загрузить данные")

# Детали одной квалификации
def qualification_detail(request, id):
    """Детали одной квалификации"""
    try:
        id = int(id)
        qualifications = load_qualifications()
        
        for q in qualifications:
            if q.get('id') == id:
                return render(request, 'qualification_detail.html', {
                    'qualification': q
                })
        
        logger.warning(f"Квалификация с id={id} не найдена")
        raise Http404("Квалификация не найдена")
        
    except Exception as e:
        logger.error(f"Ошибка в qualification_detail: {str(e)}", exc_info=True)
        raise Http404("Произошла ошибка")

def author(request):
    return render(request, 'author.html');

def shop(request):
    return render(request, 'shop.html');

def main(request):
    return render(request, 'main.html');
