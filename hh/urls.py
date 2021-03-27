from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/vacancy', views.search_vacancy),
    path('', views.index),
]
