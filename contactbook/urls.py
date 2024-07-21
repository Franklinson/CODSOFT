from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_contact, name='create_contact'),
    path('delete/<int:pk>/', views.deleteContact, name='contact_delete'),
]
