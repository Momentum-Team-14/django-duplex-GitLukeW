from unicodedata import category
from django.contrib.auth.models import AbstractUser as BaseUser
from django.conf import settings
from django.db import models

# Create your models here.


class User(BaseUser):
    # could add custom user attributes here
    pass


class Categories(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.category}'


class Flashcard(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=512)
    # related name should be the plural of the model that it's in
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='flashcards')
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f'{self.answer} in {self.question}'
