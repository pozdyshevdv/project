from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('vacancies', views.vacancies, name='vacancies'),
    path('resumes', views.resumes, name='resumes'),
    path('companies', views.companies, name='companies'),
    path('create_resume', views.create_resume, name='create_resume'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('user_profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path('vac/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('', views.index, name='index'),
]

