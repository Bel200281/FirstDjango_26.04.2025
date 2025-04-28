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

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор:</strong> <i>Иванов И. П.</i>
    """
    return HttpResponse(text)

def  about(request):
    html_content = f"""
    <p>Имя: {USER_DATA['first_name']}<br>
    Отчество: {USER_DATA['middle_name']}<br>
    Фамилия: {USER_DATA['last_name']}<br>
    Телефон: {USER_DATA['phone']}<br>
    Email: {USER_DATA['email']}</p>
    """
    return HttpResponse(html_content)