from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from .forms import CreateUserForm, CreateResumeForm, CreateVacancyForm


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


@login_required(login_url='login')
def employer(request):
    return render(request, 'employer.html', {})


@login_required(login_url='login')
def search_vacancy(request):
    query = request.GET.get('q')
    q = models.Vacancy.objects.filter(info__icontains=query).all()
    return render(request, 'search_vacancy_result.html', {
        'title': 'Поиск вакансий',
        'list_vacancy': q,
    })


@login_required(login_url='login')
def search_resume(request):
    q = models.Resume.objects.all()
    return render(request, 'search_resume_result.html', {
        'title': 'Поиск резюме',
        'list_resume': q,
    })


@login_required(login_url='login')
def create_resume(request):
    if request.method == 'POST':
        form = CreateResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.worker = request.user
            resume.save()
            messages.success(request, 'Резюме успешно создано для' + resume.profession)
            form.clean()
    else:
        form = CreateResumeForm()
    return render(request, 'create_resume.html', {
        'form': form,
    })


@login_required(login_url='login')
def create_vacancy(request):
    if request.method == 'POST':
        form = CreateVacancyForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.worker = request.user
            resume.save()
            form.clean()
    else:
        form = CreateVacancyForm()
    return render(request, 'create_resume.html', {
        'form': form,
    })
