# Generated by Django 3.0.3 on 2020-03-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20200330_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
    ]
