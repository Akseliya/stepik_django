from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'context': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Дженнифер Лоуренс', 'context': 'Биография Дженнифер Лоуренс', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'context': 'Биография Джулии Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    # передача данных в шаблон
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'women/index.html', data)  # можно context=data


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slag: {cat_slug}</p>')


def archive(request, year):
    if year > 2025:
        raise Http404()
    elif year < 1990:
        return redirect('home')
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def post_detail(request):
    if request.GET:
        result = '|'.join([f'{k}={v}' for k, v in request.GET.items()])

        return HttpResponse(result)
    else:
        return HttpResponse('GET is empty')


def about(request):
    return render(request, 'women/about.html')


def add_page(request):
    return HttpResponseNotFound('<h1>Добавить статью</h1>')


def contact(request):
    return HttpResponseNotFound('<h1>Обратная связь</h1>')


def login(request):
    return HttpResponseNotFound('<h1>Войти</h1>')
