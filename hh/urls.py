from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/vacancy', views.search_vacancy, name='search_vacancy'),
    path('search/resume', views.search_resume, name='search_resume'),
    path('employer', views.employer, name='employer'),
    path('', views.index, name='index'),
]
