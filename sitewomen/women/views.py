from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from women.models import Women, Category, TagPost

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

data_db = [
    {"id": 1, "title": "Анджелина Джоли", "context": "Биография Анджелины Джоли", "is_published": True},
    {"id": 2, "title": "Дженнифер Лоуренс", "context": "Биография Дженнифер Лоуренс", "is_published": False},
    {"id": 3, "title": "Джулия Робертс", "context": "Биография Джулии Робертс", "is_published": True},
]


def index(request):
    posts = Women.published.all()

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'menu': menu,
        'title': post.title,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'women/post.html', data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponseNotFound("<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)
