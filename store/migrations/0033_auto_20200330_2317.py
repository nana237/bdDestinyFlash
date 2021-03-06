# Generated by Django 3.0.3 on 2020-03-30 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_auto_20200330_2157'),
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
            name='LIVRAISON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateL', models.DateField()),
                ('descriptionL', models.CharField(max_length=100)),
                ('montantL', models.IntegerField()),
                ('typeL', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.CLIENT')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.COMMANDE')),
                ('livreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.LIVREUR')),
                ('point_de_retrait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.POINT_DE_RETRAIT')),
            ],
        ),
    ]
