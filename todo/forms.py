from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
        

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description here'}),
        }
        

class EditTodo(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description here'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }