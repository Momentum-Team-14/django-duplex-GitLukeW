from django.urls import path
from . import views

urlpatterns = [
    #Categories
    path('', views.categories_list, name='categories_list'),
    path('category/<int:pk>', views.categories_detail, name='categories_detail'),
    path('categories/new/', views.categories_new, name='categories_new'),
    path('categories/<int:pk>/edit/', views.categories_edit, name='categories_edit'),
    path('categories/<pk>/remove/', views.category_remove, name='category_remove'),

    #Flashcards
    path('', views.flashcard_list, name='flashcard_list'),
    path('flashcards/<int:pk>', views.flashcard_detail, name='flashcard_detail'),
    path('flashcard/new/', views.flashcard_new, name='flashcard_new'),
    path('flashcards/<int:pk>/edit/', views.flashcard_edit, name='flashcard_edit'),
    path('flashcards/<pk>/remove/', views.flashcard_remove, name='flashcard_remove'),
    path('flashcards/<int:pk>', views.flashcard_view, name='flashcard_view'),
]