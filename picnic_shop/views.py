from django.shortcuts import render
import json
from django.http import Http404

# Загрузка данных из JSON
def load_qualifications():
    with open('picnic_shop/dump.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Список всех квалификаций
def qualifications_list(request):
    qualifications = load_qualifications()
    return render(request, 'qualifications_list.html', {'qualifications': qualifications})

# Детали одной квалификации
def qualification_detail(request, id):
    qualifications = load_qualifications()
    qualification = next((q for q in qualifications if q['id'] == id), None)
    
    if not qualification:
        raise Http404("Квалификация не найдена")
    
    return render(request, 'qualification_detail.html', {'qualification': qualification})

def author(request):
    return render(request, 'author.html');

def shop(request):
    return render(request, 'shop.html');

def main(request):
    return render(request, 'main.html');