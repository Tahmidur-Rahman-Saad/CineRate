# Generated by Django 3.2.6 on 2025-01-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
