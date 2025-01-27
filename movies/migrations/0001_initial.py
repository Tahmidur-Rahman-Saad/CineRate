# Generated by Django 3.2.6 on 2025-01-15 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('criteria', models.CharField(choices=[('U', 'Universal'), ('PG', 'Parental Guidance'), ('12A', '12A'), ('15', '15'), ('18', '18')], max_length=10)),
                ('language', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=200)),
                ('budget', models.FloatField(help_text='Enter in Lakh', max_length=10)),
                ('total_collection', models.FloatField(help_text='Enter in Lakh', max_length=10)),
                ('final_verdict', models.CharField(choices=[('F', 'Flop'), ('A', 'Average'), ('H', 'Hit'), ('B', 'Blockbuster')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_images/')),
                ('casts', models.ManyToManyField(related_name='movies', to='accounts.Cast')),
                ('director', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='accounts.director')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('singers', models.TextField(max_length=50)),
                ('publish_date', models.DateField()),
                ('lyrics', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
