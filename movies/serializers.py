from rest_framework import serializers
from .models import Movie,Music
from accounts.serializers import CastSerializer,DirectorSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDirectorCastSerializer(serializers.ModelSerializer):
    cast = CastSerializer()
    director = DirectorSerializer()
    class Meta:
        model = Movie
        fields = ['name','release_date','criteria','language','discription','budget','total_collection','final_verdict','image']


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


