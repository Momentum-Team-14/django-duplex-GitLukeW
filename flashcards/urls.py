from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('flashcards/<int:pk>', views.flashcards_detail, name='flashcards_detail'),
    path('flashcards/new/', views.flashcard_new, name='flashcard_new'),
    path('flashcards/<int:pk>/edit/', views.flashcard_edit, name='flashcard_edit'),
    path('flashcards/<pk>/remove/', views.flashcard_remove, name='flashcard_remove'),
]