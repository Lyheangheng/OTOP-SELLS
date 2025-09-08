import json
from django.shortcuts import render
import os

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def food_places(request):
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'otop.json')
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)
    places = data.get('Sheet1', [])
    return render(request, 'food_places.html', {'places': places})
