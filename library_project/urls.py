from django.contrib import admin
from django.urls import path, include
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # URL для отображения главной страницы
    path('add_publisher/', views.add_publisher, name='add_publisher'), 
    path('add_book/', views.add_book, name='add_book'),
    path('add_reader/', views.add_reader, name='add_reader'), 
    path('add_loan/', views.add_loan, name='add_loan'),
    # Добавьте другие URL-шаблоны здесь
] 