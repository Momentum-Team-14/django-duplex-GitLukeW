from django import forms
from .models import Categories, Flashcard


class FlashcardsForm(forms.ModelForm):

    class Meta:
        model = Flashcard
        fields = ('question', 'answer', 'category',)


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('category',)
