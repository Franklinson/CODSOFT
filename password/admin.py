from django.contrib import admin
from .models import Password

# Register your models here.
admin.site.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('password', 'created_at')