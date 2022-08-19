from django.shortcuts import render
from django.views import generic
from . models import Todo
# Create your views here.

class TodoList(generic.ListView):
    model = Todo
    template_name ="todo.html"

class DetailTodo(generic.UpdateView):
    model = Todo
    template_name = "detail.html"
