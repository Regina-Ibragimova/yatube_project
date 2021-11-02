# posts/urls.py
from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
#главная страница
    path('', views.index, name='index'),
    #Список групп
    path('group/', views.group_list, name='group_list'),

    path('group/<slug:slug>/', views.group_post, name='group_post'),
] 