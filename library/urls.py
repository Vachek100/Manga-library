from django.urls import path
from . import views

urlpatterns = [
    path('', views.manga_list, name='manga_list'),
    path('manga/<int:pk>/', views.manga_detail, name='manga_detail'),
    path('manga/<int:pk>/borrow/', views.borrow_manga, name='borrow_manga'),
    path('manga/<int:pk>/return/', views.return_manga, name='return_manga'),
]
