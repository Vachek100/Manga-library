from django.urls import path
from . import views

urlpatterns = [
    path('', views.manga_list, name='manga_list'),
    path('<int:pk>/', views.manga_detail, name='manga_detail'),
]
