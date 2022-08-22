from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from . models import Todo
from . form import TodoForm
# Create your views here.



def todoList(request):
    form = TodoForm()
    if(request.method == "GET"):
        query_set = Todo.objects.all()
        todos = query_set.filter(completed = False)[:5]
        completed = query_set.filter(completed = True)[:5]
        context = {"form": form, "todos": todos, "completed": completed }
        return render(request, "todo.html", context)

def createTodo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # print("is working")
            return redirect("list-todo")
        else:
            # print("something is not working")
            return redirect("list-todo")


class EditTodo(UpdateView):
    model = Todo
    template_name = 'edit-todo.html'
    form_class = TodoForm
    success_url = reverse_lazy('list-todo')


def deleteTodo(request, pk):
   todo_instance = Todo.objects.get(pk =pk)
   todo_instance.delete()
   return redirect('list-todo')