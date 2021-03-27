from django.shortcuts import render
from django.http.response import HttpResponse
from . import models


def index(request):
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def search_vacancy(request):
    q = models.Vacancy.objects.all()
    return render(request, 'search_vacancy_result.html', {
        'title': 'Поиск работы',
        'list_vacancy': q,
    })