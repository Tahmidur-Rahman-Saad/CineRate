from django.db import models
from accounts.models import Reviewer
from movies.models import Movie

# Create your models here.
class Rating(models.Model):
    rating = models.IntegerField(default=5, help_text="Enter star 1 to 5")
    review = models.CharField(max_length=200)
    reviewer = models.OneToOneField(Reviewer, on_delete=models.CASCADE, related_name='reviewers', null = True)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name='movies', null = True)