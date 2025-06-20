
from django.shortcuts import render
from django.http import Http404
import json
import os
import logging
from django.conf import settings

# Настройка логгера
logger = logging.getLogger(__name__)

def load_qualifications():
    """Загрузка данных из JSON"""
    try:
        # Абсолютный путь к файлу
        json_path = os.path.join(settings.BASE_DIR, 'picnic_shop', 'dump.json')
        
        # Проверка существования файла
        if not os.path.exists(json_path):
            logger.error(f"Файл не найден: {json_path}")
            raise FileNotFoundError("Файл данных отсутствует")
        
        # Чтение JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Преобразование структуры (pk → id)
        processed_data = []
        for item in data:
            if isinstance(item, dict) and 'pk' in item and 'fields' in item:
                new_item = {'id': item['pk']}
                new_item.update(item['fields'])
                processed_data.append(new_item)
        
        if not processed_data:
            logger.warning("JSON загружен, но список пуст")
        
        return processed_data
        
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка в формате JSON: {str(e)}")
        raise ValueError("Неверный формат JSON")
    except Exception as e:
        logger.error(f"Ошибка загрузки данных: {str(e)}")
        raise

def qualifications_list(request):
    """Список всех учреждений"""
    try:
        qualifications = load_qualifications()
        return render(request, 'qualifications_list.html', {
            'qualifications': qualifications
        })
    except Exception as e:
        logger.error(f"Ошибка в qualifications_list: {str(e)}")
        raise Http404("Не удалось загрузить данные")

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
