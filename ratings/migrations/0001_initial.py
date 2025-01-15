# Generated by Django 3.2.6 on 2025-01-15 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=5, help_text='Enter star 1 to 5', max_length=1)),
                ('review', models.CharField(max_length=200)),
                ('movie', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='movies.movie')),
                ('reviewer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='accounts.reviewer')),
            ],
        ),
    ]
