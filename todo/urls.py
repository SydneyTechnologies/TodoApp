from django.urls import path
from .views import todoList, createTodo, EditTodo, deleteTodo, completeTodo
urlpatterns = [
    path('', todoList, name="list-todo"),
    path('<int:pk>/edit', EditTodo.as_view(), name= "edit-todo"),
    path('<int:pk>/delete', deleteTodo, name="delete-todo"),
    path('<int:pk>/complete', completeTodo, name="complete-todo"),
    path('create', createTodo, name="create"),
]