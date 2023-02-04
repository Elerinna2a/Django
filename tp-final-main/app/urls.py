from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="home"),
    # List
    path('entreprises/', entreprises, name='entreprises'),
    path('clients/', clients, name='clients'),
    path('reclamations/', reclamations, name='reclamations'),
    # Detail
    path('entreprises/<int:pk>/', entreprise, name='entreprise'),
    path('clients/<int:pk>/', client, name='client'),
    path('reclamations/<int:pk>/', reclamation, name='reclamation'),
    # Create
    path('entreprises/create/', create_entreprise, name='create-entreprise'),
    path('clients/create/', create_client, name='create-client'),
    path('reclamations/create/', create_reclamation, name='create-reclamation'),
    # Update
    path('entreprises/update/<int:pk>/', update_entreprise, name='update-entreprise'),
    path('clients/update/<int:pk>/', update_client, name='update-client'),
    path('reclamations/update/<int:pk>/', update_reclamation, name='update-reclamation'),
    # Delete
    path('entreprises/delete/<int:pk>/', delete_entreprise, name='delete-entreprise'),
    path('clients/delete/<int:pk>/', delete_client, name='delete-client'),
    path('reclamations/delete/<int:pk>/', delete_reclamation, name='delete-reclamation'),
    # Validate
    path('reclamations/validate/<int:pk>/', validate_reclamation, name='validate-reclamation'),
    path('reclamations/devalidate/<int:pk>/', devalidate_reclamation, name='devalidate-reclamation'),
]