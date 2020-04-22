# Generated by Django 3.0.3 on 2020-03-30 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_auto_20200330_2348'),
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
            name='NOTIFICATION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raisonNot', models.CharField(max_length=100)),
                ('dateNot', models.DateField(max_length=100)),
                ('agent_destiny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.AGENT_DESTINY')),
                ('prestataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.PRESTATAIRE')),
            ],
        ),
        migrations.AddField(
            model_name='agent_destiny',
            name='prestataires',
            field=models.ManyToManyField(through='store.NOTIFICATION', to='store.PRESTATAIRE'),
        ),
    ]