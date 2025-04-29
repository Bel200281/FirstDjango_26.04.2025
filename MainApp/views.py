from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

USER_DATA = {
    'first_name': 'Иван',
    'middle_name':'Петрович',
    'last_name': 'Иванов',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
}
ITEMS = [
    {"id": 1, "name": "Кроссовки Abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Coca-Cola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"},  
]



def home(request):
    text = f"""
    <h1>Изучаем django</h1>
    <strong>Автор:</strong> <a href="/about/"><i>{USER_DATA['first_name']} {USER_DATA['middle_name']} {USER_DATA['last_name']}</i></a>

    """
    
    items = ITEMS
    html_content = '<h1>Товары:</h1>'
    html_content += '<ul>'
    for item in items:
        html_content += f'<li><a href="/item/{item["id"]}/">{item["name"]}</a></li>'
    html_content += '</ul>'
    
    return HttpResponse(text + html_content)

def  about(request):
    html_content = f"""
    <p>Имя: {USER_DATA['first_name']}<br>
    Отчество: {USER_DATA['middle_name']}<br>
    Фамилия: {USER_DATA['last_name']}<br>
    Телефон: {USER_DATA['phone']}<br>
    Email: {USER_DATA['email']}</p>
    """
    return HttpResponse(html_content)

def show_item(request, item_id):
    found_items = [item for item in ITEMS if item["id"]== int(item_id)]
    if found_items:
        item = found_items[0]
        return HttpResponse (f"<h2>Название товара: {item['name']}</h2>")
    else:
        return HttpResponse (f"Товара с номером: {item_id} не найден.", status= 404)
    