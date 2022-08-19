from django.urls import path
from .views import todoList, createTodo
urlpatterns = [
    path('', todoList, name="todo-list"),
    path('<int:pk>', todoList, name="todo-list"),
    path('create', createTodo, name="create"),
]