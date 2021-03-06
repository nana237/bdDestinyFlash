# Generated by Django 3.0.3 on 2020-03-31 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_auto_20200331_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristique',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ARTICLE'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='articles',
            field=models.ManyToManyField(to='store.ARTICLE'),
        ),
        migrations.CreateModel(
            name='FACTURE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateF', models.DateField(default=datetime.date.today)),
                ('montantF', models.IntegerField()),
                ('commande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.COMMANDE')),
            ],
        ),
    ]
