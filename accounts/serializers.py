from rest_framework import serializers
from .models import Reviewer,Director,Cast,Authorizer
from django.contrib.auth.models import User


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'


class AuthorizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorizer
        fields = '__all__'
