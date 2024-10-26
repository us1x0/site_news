from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse( "<h1>Новости NowTIME🪶</h1>"
                         "<hr>"
                         "<a href='/news/'> ⭕️Жаркие новости на сегодня➡️ </a>"
                         "<br>"
                         "<br>"
                         "<a href='/contacts/'> Контакты ☎️ </a> ")
def news_today(request):
    return HttpResponse('<h3>Какие новости на сегодня ⁉️</h3>'
                        '<hr>'
                        '<a href="/contacts/"> Контакты ☎️ </a>')

def contacts(request):
    return HttpResponse('<h4>Контакты ☎️</h4>'
                        '<hr>'
                        '<h5>nowtime@gmail.com 📩</h5>'
                        '<h6>Принимаем самые горячие новости🔥</h6>'
                        '<h6><a href="/"> Вернуться на ГЛАВНУЮ СТРАНИЦУ⬅️</a></h6>')
