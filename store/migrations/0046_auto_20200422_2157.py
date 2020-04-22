# Generated by Django 3.0.3 on 2020-04-22 19:57

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_auto_20200422_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photoAr',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.upload_path),
        ),
        migrations.AlterField(
            model_name='caracteristique',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ARTICLE'),
        ),
        migrations.AlterField(
            model_name='caracteristique',
            name='photoCaract',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to=store.models.upload_caracteristique),
        ),
        migrations.AlterField(
            model_name='commande',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, to='store.ARTICLE'),
        ),
    ]
