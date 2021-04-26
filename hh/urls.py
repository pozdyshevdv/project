from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('vacancy', views.search_vacancy, name='search_vacancy'),
    path('create_resume', views.create_resume, name='create_resume'),
    path('search/resume', views.search_resume, name='search_resume'),
    path('employer', views.employer, name='employer'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.index, name='index'),
]
