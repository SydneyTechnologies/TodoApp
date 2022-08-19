from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from . models import Todo
from . form import TodoForm
# Create your views here.



def todoList(request, pk=None):
    form = TodoForm()
    target = request.session['target'] = pk
    if target != None:
        todo = Todo.objects.get(pk=target)
        form = TodoForm(instance=todo)
    if(request.method == "GET"):
        set = Todo.objects.all()
      
        query_set = set[0: len(set)] if len(set) < 3 else set[len(set) -3 : len(set)]
        context = {"form": form, "todos": query_set}
        return render(request, "todo.html", context)

def createTodo(request):
    form = TodoForm()
    target = request.session.get('target', None)
    if request.method == "POST":
        if  target != None: 
            form = TodoForm(request.POST, instance = Todo.objects.get(pk=target))
        else:
            form = TodoForm(request.POST)
        if form.is_valid():
            target = request.session['target'] = None
            form.save()
            return redirect("todo-list")
        else:
            return redirect("todo-list")
    else:
        return HttpResponse("not working men")