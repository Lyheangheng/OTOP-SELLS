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
    places = []
    for place in data.get('Sheet1', []):
        places.append({
            'product_name': place.get('ชื่อสินค้า OTOP', ''),
            'place_name': place.get('ชื่อสถานที่จัดจำหน่าย', ''),
            'address': place.get('ที่อยู่', ''),
            'district': place.get('อำเภอ', ''),
            'province': place.get('จังหวัด', ''),
            'phone': place.get('เบอร์โทรศัพท์', ''),
            'LAT': place.get('LAT', None),
            'LONG': place.get('LONG', None),
        })
    return render(request, 'food_places.html', {'places': places})
