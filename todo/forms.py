from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    
    class meta:
        model = Todo
        fields = ['title', 'description']