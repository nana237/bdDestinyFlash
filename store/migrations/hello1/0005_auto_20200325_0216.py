# Generated by Django 3.0.3 on 2020-03-25 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_movie_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title']},
        ),
    ]
