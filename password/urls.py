from django.urls import path
from . import views

urlpatterns = [
     path('password_generator/', views.password_generator_view, name='password_generator'),
     path('delete/<int:pk>/', views.deletePassword, name='deletePassword'),
]
 
 
 
