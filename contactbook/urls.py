from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_contact, name='create_contact'),
    path('deletecontact/<int:pk>/', views.deleteContact, name='contact_delete'),
    path('edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
]
