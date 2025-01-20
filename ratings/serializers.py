from rest_framework import serializers
from .models import Rating
from movies.serializers import MovieSerializer
from accounts.serializers import ReviewerSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


#nested serializer shows all data
class RatingMovieReviewerSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    reviewer = ReviewerSerializer()

    class Meta:
        model = Rating
        fields = ['id','rating','review']


