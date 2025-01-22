from rest_framework import serializers
from .models import Reviewer,Director,Cast,Authorizer
from django.contrib.auth.models import User

    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 


class ReviewerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Reviewer
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Director
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cast
        fields = '__all__'


class AuthorizerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Authorizer
        fields = '__all__'
