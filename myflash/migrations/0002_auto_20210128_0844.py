# Generated by Django 3.1.5 on 2021-01-28 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myflash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcards',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='flashcards',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]