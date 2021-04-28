from django.urls import path, include
from . import views

urlpatterns = [
    path('favorites/', include([
        path('', views.favorites_list, name='favorites_list'),
        path('<int:pk>/add/', views.add_to_favorites, name='add_to_favorites'),
        path('<int:pk>/remove/', views.remove_from_favorites, name='remove_from_favorites'),
        path('delete/', views.delete_favorites, name='delete_favorites'),
    ]))
]
