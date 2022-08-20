from django.urls import path
from .views import todoList, createTodo, EditTodo, deleteTodo
urlpatterns = [
    path('', todoList, name="list-todo"),
    path('<int:pk>/edit', EditTodo.as_view(), name= "edit-todo"),
    path('<int:pk>/delete', deleteTodo, name="delete-todo"),
    path('create', createTodo, name="create"),
]