from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList, name='todo_list'),
    path('<int:pk>/', views.TodoDetail, name='todo_detail'),
    path('create/', views.createTodo, name='todo_create')
]
