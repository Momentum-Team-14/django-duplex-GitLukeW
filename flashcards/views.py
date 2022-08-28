from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard, Categories
from .forms import FlashcardsForm, CategoriesForm



def categories_list(request):
    category = Categories.objects.all()
    return render(request, 'flashcards/categories_list.html', {'categories': category})


def categories_detail(request, pk):
    categories = get_object_or_404(Categories, pk=pk)
    return render(request, 'flashcards/categories_detail.html', {"categories": categories})


def categories_new(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            categories = form.save(commit=False)
            categories.author = request.user
            categories.save()
            return redirect('categories_detail', pk=categories.pk)
    else:
        form = CategoriesForm()
    return render(request, 'flashcards/categories_edit.html', {'form': form})


def categories_edit(request, pk):
    post = get_object_or_404(Categories, pk=pk)
    if request.method == "POST":
        form = CategoriesForm(request.POST, instance=post)
        if form.is_valid():
            categories = form.save()
            return redirect('categories_detail', pk=post.pk)
    else:
        form = CategoriesForm(instance=post)
    return render(request, 'flashcards/categories_edit.html', {'form': form})


def category_remove(request, pk):
    post = get_object_or_404(Categories, pk=pk)
    post.delete()
    return redirect('categories_list')


def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/categories_detail.html', {'flashcards': flashcards})


def flashcard_detail(request, pk):
    flashcards = get_object_or_404(Flashcard, pk=pk)
    return render(request, 'flashcards/flashcard_detail.html', {"flashcards": flashcards})


def flashcard_new(request):
    if request.method == "POST":
        form = FlashcardsForm(request.POST)
        if form.is_valid():
            flashcards = form.save(commit=False)
            flashcards.author = request.user
            flashcards.save()
            return redirect('flashcard_detail.html', pk=flashcards.pk)
    else:
        form = FlashcardsForm()
    return render(request, 'flashcards/flashcard_edit.html', {'form': form})


def flashcard_edit(request, pk):
    post = get_object_or_404(Flashcard, pk=pk)
    if request.method == "POST":
        form = FlashcardsForm(request.POST, instance=post)
        if form.is_valid():
            flashcard = form.save()
            return redirect('flashcard_detail', pk=post.pk)
    else:
        form = FlashcardsForm(instance=post)
    return render(request, 'flashcards/flashcard_edit.html', {'form': form})


def flashcard_remove(request, pk):
    post = get_object_or_404(Flashcard, pk=pk)
    post.delete()
    return redirect('flashcard_list')
