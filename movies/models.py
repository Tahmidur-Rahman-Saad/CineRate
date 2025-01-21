from django.db import models
from accounts.models import Cast,Director

# Create your models here.

class Movie(models.Model):
    CRITERIA_CHOICES = [
        ('U', 'Universal'),
        ('PG', 'Parental Guidance'),
        ('12A', '12A'),
        ('15', '15'),
        ('18', '18'),
    ]

    FINAL_VERDICT_CHOICES = [
        ('F', 'Flop'),
        ('A', 'Average'),
        ('H', 'Hit'),
        ('B', 'Blockbuster'),
    ]


    name = models.CharField(max_length=100)
    release_date = models.DateField()
    criteria = models.CharField(max_length=10,choices=CRITERIA_CHOICES)
    language = models.CharField(max_length=50)
    discription = models.TextField(max_length=200)
    budget = models.FloatField(max_length=10,help_text="Enter in Lakh")
    total_collection = models.FloatField(max_length=10,help_text="Enter in Lakh")
    final_verdict = models.CharField(max_length=10,choices=FINAL_VERDICT_CHOICES)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    casts = models.ManyToManyField(Cast, related_name='movies')
    director = models.OneToOneField(Director,on_delete=models.CASCADE, related_name='director', null = True)
    rating = models.FloatField(max_length=5,default=)



    
class Music(models.Model):
    name = models.CharField(max_length=100 )
    singers = models.TextField(max_length=50)
    publish_date = models.DateField()
    lyrics = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,null=None)
