from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard, Categories
from .forms import FlashcardsForm, CategoriesForm
from django.contrib.auth.decorators import login_required


@login_required
def categories_list(request):
    category = Categories.objects.filter(user=request.user)
    return render(request, 'flashcards/categories_list.html', {'categories': category})

@login_required
def categories_detail(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'flashcards/categories_detail.html', {"category": category, 'flashcards': category.flashcards.all()})

@login_required
def categories_new(request):
    if request.method == "POST":
        category_form = CategoriesForm(request.POST)
        if category_form.is_valid():
            categories = category_form.save(commit=False)
            categories.user = request.user
            categories.save()
            return redirect('categories_detail', pk=categories.pk)
    else:
        category_form = CategoriesForm()
    return render(request, 'flashcards/categories_edit.html', {'category_form': category_form})

@login_required
def categories_edit(request, pk):
    post = get_object_or_404(Categories, pk=pk)
    if request.method == "POST":
        category_form = CategoriesForm(request.POST, instance=post)
        if category_form.is_valid():
            categories = category_form.save()
            return redirect('categories_detail', pk=post.pk)
    else:
        category_form = CategoriesForm(instance=post)
    return render(request, 'flashcards/categories_edit.html', {'category_form': category_form})

@login_required
def category_remove(request, pk):
    post = get_object_or_404(Categories, pk=pk)
    post.delete()
    return redirect('categories_list')

@login_required
def flashcard_list(request):
    flashcards = Flashcard.objects.filter(user=request.user)
    return render(request, 'flashcards/categories_detail.html', {'flashcards': flashcards})


@login_required
def flashcard_detail(request, pk):
    flashcards = get_object_or_404(Flashcard, pk=pk)
    return render(request, 'flashcards/flashcard_detail.html', {"flashcards": flashcards})

@login_required
def flashcard_new(request):
    if request.method == "POST":
        flashcard_form = FlashcardsForm(request.POST)
        if flashcard_form.is_valid():
            flashcard = flashcard_form.save(commit=False)
            flashcard.user = request.user
            flashcard.save()
            return redirect('flashcard_detail', pk=flashcard.pk)
    else:
        flashcard_form = FlashcardsForm()
    return render(request, 'flashcards/flashcard_edit.html', {'flashcard_form': flashcard_form})

@login_required
def flashcard_edit(request, pk):
    post = get_object_or_404(Flashcard, pk=pk)
    if request.method == "POST":
        flashcard_form = FlashcardsForm(request.POST, instance=post)
        if flashcard_form.is_valid():
            flashcard = flashcard_form.save()
            return redirect('flashcard_detail', pk=post.pk)
    else:
        flashcard_form = FlashcardsForm(instance=post)
    return render(request, 'flashcards/flashcard_edit.html', {'flashcard_form': flashcard_form})

@login_required
def flashcard_remove(request, pk):
    post = get_object_or_404(Flashcard, pk=pk)
    post.delete()
    return redirect('flashcard_list')

@login_required
def flashcard_view(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    flashcards = category.flashcards.all()
    return render(request, 'flashcards/categories_detail.html', {'flashcards': flashcards})


