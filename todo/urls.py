from django.urls import path
from .views import todoList, createTodo, EditTodo
urlpatterns = [
    path('', todoList, name="todo-list"),
    path('<int:pk>', todoList, name="todo-list"),
    path('<int:pk>/edit', EditTodo.as_view(), name= "edit-todo"),
    path('create', createTodo, name="create"),
]