from django import forms

from .models import Flashcard


class FlashcardsForm(forms.ModelForm):

    class Meta:
        model = Flashcard
        fields = ('question', 'answer', 'category', 'user')
