
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('del/<int:pk>/', views.delete_todo, name='delete_todo'),

    path('create/', views.create_todo, name='create_todo'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
]
