from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import *


def TodoList(request):
    todos = Todo.objects.all()
    total = todos.count()
    completed = Todo.objects.filter(completed=True).count()
    
    context = {
        'todos': todos,
        'total': total,
        'completed': completed,
    }
    return render(request, 'todo_list.html', context)


def TodoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todo_detail.html', context)


def createTodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    context = {
        'form': form,
    }
    return render(request, 'todo_form.html', context)


def editTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = EditTodo(instance=todo)
    if request.method == 'POST':
        form = EditTodo(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', pk=todo.pk)  # Pass the pk argument here
    context = {
        'form': form,
    }
    return render(request, 'edit_todo.html', context)


def deleteTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'delete.html', {'rem': todo})