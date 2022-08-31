# Generated by Django 4.1 on 2022-08-31 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_alter_flashcard_answer_alter_flashcard_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='user',
        ),
        migrations.AddField(
            model_name='categories',
            name='user',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
            preserve_default=b'I01\n',
        ),
    ]