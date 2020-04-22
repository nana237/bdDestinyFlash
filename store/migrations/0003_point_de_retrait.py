# Generated by Django 3.0.3 on 2020-03-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_article_movie_person_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='POINT_DE_RETRAIT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libPoint', models.CharField(max_length=100)),
                ('villePoint', models.CharField(max_length=100)),
                ('quartierPoint', models.CharField(max_length=100)),
                ('descriptionPoint', models.CharField(max_length=256)),
                ('telPoint', models.IntegerField()),
                ('mailPoint', models.EmailField(max_length=254)),
            ],
        ),
    ]
