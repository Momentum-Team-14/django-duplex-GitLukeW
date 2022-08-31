from unicodedata import category
from django.contrib.auth.models import AbstractUser as BaseUser
from django.conf import settings
from django.db import models
from pickle import TRUE

# Create your models here.


class User(BaseUser):
    # could add custom user attributes here
    pass


class Categories(models.Model):
    category = models.CharField(max_length=250)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name= 'categories', null=TRUE)

    def __str__(self):
        return f'{self.category}'


class Flashcard(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='flashcards')
    question = models.CharField(max_length=512)
    answer = models.TextField()
    

    def __str__(self):
        return f'{self.question} {self.answer}'
