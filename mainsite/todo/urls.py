from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Homepage'),
    path('finish/<int:pk>/', views.finish, name='finish'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('admin/', admin.site.urls)
]