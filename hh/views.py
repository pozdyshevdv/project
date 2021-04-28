from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from django.db.models import Q
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
                messages.success(request, 'Аккаунт создан для ' + user)
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
                if username == '' or password == '':
                    messages.info(request, 'Необходимо заполнить все поля ')
                else:
                    messages.info(request, 'Неправильный логин или пароль ')

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
def vacancies(request):
    query = request.GET.get('q')
    if query:
        all_vacancies = models.Vacancy.objects.filter(
            Q(company_name__icontains=query) |
            Q(profession__icontains=query) | Q(info__icontains=query)
        ).all
    else:
        all_vacancies = models.Vacancy.objects.all()
    context = {
        'all_vacancies': all_vacancies,
        'favorites_list': request.session.get('favorites'),
    }
    return render(request, 'vacancies.html', context)


@login_required(login_url='login')
def vacancy_detail(request, pk):
    vacancy = models.Vacancy.objects.get(id=pk)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'vacancy_detail.html', context)


@login_required(login_url='login')
def resumes(request):
    query = request.GET.get('q')
    if query:
        all_resumes = models.Resume.objects.filter(
            Q(last_name__icontains=query) | Q(first_name__icontains=query) |
            Q(profession__icontains=query) | Q(info__icontains=query)
        ).all
    else:
        all_resumes = models.Resume.objects.all()
    context = {
        'all_resumes': all_resumes,
    }
    return render(request, 'resumes.html', context)


@login_required(login_url='login')
def resume_detail(request, pk):
    resume = models.Resume.objects.get(id=pk)
    context = {
        'resume': resume,
    }
    return render(request, 'resume_detail.html', context)


@login_required(login_url='login')
def companies(request):
    all_companies = models.User.objects.all()
    context = {
        'all_companies': all_companies,
    }
    return render(request, 'companies.html', context)


@login_required(login_url='login')
def user_profile(request, pk):
    user = models.User.objects.get(id=pk)
    user_resumes = models.Resume.objects.filter(worker=user).all()
    user_vacancies = models.Vacancy.objects.filter(employer=user).all()
    return render(request, 'user_profile.html', {
        'title': 'Личный кабинет',
        'user': user,
        'user_resumes': user_resumes,
        'user_vacancies': user_vacancies,
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
