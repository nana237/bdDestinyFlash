# Generated by Django 3.0.3 on 2020-03-29 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20200330_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='StockSecuriteAr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='VideoPubAr',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='article',
            name='designationAr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.MARQUE'),
        ),
        migrations.AlterField(
            model_name='article',
            name='nbAchatAr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='panier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.PANIER'),
        ),
        migrations.AlterField(
            model_name='article',
            name='photoAr',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='article',
            name='prixAr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='qteAr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='sous_categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.SOUS_CATEGORIE'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
    ]
