import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from .models import Password
from .forms import PasswordForm

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator_view(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            password = generate_password(length)
            Password.objects.create(password=password)
            return redirect('home')
    else:
        form = PasswordForm()
    return render(request, 'password_generator.html', {'form': form})


def deletePassword(request, pk):
    genpass = get_object_or_404(Password, pk=pk)
    if request.method == 'POST':
        Password.delete()
        return redirect('todo_list')
    return render(request, 'delete.html', {'rem': genpass})