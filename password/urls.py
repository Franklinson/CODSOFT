from django.urls import path
from . import views

urlpatterns = [
     path('password_generator/', views.password_generator_view, name='password_generator'),
     path('deletepass/<int:pk>/', views.deletePassword, name='deletePassword'),
]
 
 
 
