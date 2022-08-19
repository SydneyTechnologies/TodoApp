from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from . models import Todo
from . form import TodoForm
# Create your views here.

# class TodoList(generic.ListView):
#     model = Todo
#     template_name ="todo.html"

class DetailTodo(generic.UpdateView):
    model = Todo
    template_name = "detail.html"


def todoList(request):
    form = TodoForm()
    if(request.method == "GET"):
        set = Todo.objects.all()
        query_set = set[len(set)-3: len(set)]
        context = {"form": form, "todos": query_set}
        return render(request, "todo.html", context)

def createTodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
        else:
            return redirect("todo-list")
    else:
        return HttpResponse("not working men")
