# Generated by Django 3.2.6 on 2025-01-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=5, help_text='Enter star 1 to 5'),
        ),
    ]
