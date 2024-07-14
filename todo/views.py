from django.shortcuts import render
from .models import Todo


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