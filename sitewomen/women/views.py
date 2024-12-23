from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Страница приложения women.')


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
