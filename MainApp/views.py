from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# Create your views here.

USER_DATA = {
    'first_name': 'Иван',
    'middle_name':'Петрович',
    'last_name': 'Иванов',
    'phone': '8-923-600-01-02',
    'email': 'vasya@mail.ru'
}
ITEMS = [
    {"id": 1, "name": "Кроссовки Adidas","quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-Cola 1 литр", "quantity": 3},
    {"id": 4, "name": "Картофель фри", "quantity": 4},
    {"id": 5, "name": "Кепка", "quantity": 1},  
]

def list_items(request):
    return render(request, 'index.html', {'items': ITEMS})



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

    back_link = '<p><a href="/">Вернуться на главную страницу</a></p>'
    
    return HttpResponse(html_content+ back_link)

def show_item(request, item_id):
    found_items = [item for item in ITEMS if item["id"]== int(item_id)]
    if found_items:
        item = found_items[0]
        content = f"""
        <h2>Название товара: {item['name']}</h2>
        <a href="/items/">Назад к списку товаров</a>
        """
        return HttpResponse (content)
    else:
        return HttpResponse (f"Товара с номером: {item_id} не найден.", status= 404)
    

def item_list(request):
    html_content = '<h1>Товары:</h1>'
    item_html = '<ol>'
    for item in ITEMS:
        item_html += f'<li><a href="/item/{item["id"]}/">{item["name"]}</a></li>'
    item_html += '</ol>'

    item_html += '<p><a href="/">Вернуться на главную страницу</a></p>'
    return HttpResponse(html_content+item_html)

def show_item(request, item_id):
    item = (Item, pk=item_id)
    context = {'item': item}
    return render(request, 'index.html', context)




