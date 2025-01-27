# Generated by Django 3.2.6 on 2025-01-28 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20250127_1156'),
        ('movies', '0004_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='casts',
            field=models.ManyToManyField(blank=True, related_name='movies', to='accounts.Cast'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='accounts.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
