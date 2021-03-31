from django.shortcuts import render
from django.http.response import HttpResponse
from . import models


def index(request):
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def employer(request):
    return render(request, 'employer.html', {})


def search_vacancy(request):
    query = request.GET.get('q')
    q = models.Vacancy.objects.filter(info__icontains=query).all()
    return render(request, 'search_vacancy_result.html', {
        'title': 'Поиск вакансий',
        'list_vacancy': q,
    })


def search_resume(request):
    q = models.Resume.objects.all()
    return render(request, 'search_resume_result.html', {
        'title': 'Поиск резюме',
        'list_resume': q,
    })