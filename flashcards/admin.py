from django.contrib import admin
from .models import User, Flashcard, Categories

# #Register your models here.

admin.site.register(Flashcard)
admin.site.register(User)
admin.site.register(Categories)
