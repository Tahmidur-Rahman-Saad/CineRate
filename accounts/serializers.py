from rest_framework import serializers
from .models import Reviewer,Director,Cast,Authorizer
from django.contrib.auth.models import User
 
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ReviewerReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Reviewer
        fields = '__all__'


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'


class DirectorReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Director
        fields = '__all__' 


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__' 


class CastReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cast
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'


class AuthorizerReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Authorizer
        fields = '__all__'


class AuthorizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorizer
        fields = '__all__'


# #custom serializer for retrieving customer or admin data
# class UserReadSerializer(serializers.ModelSerializer):
#     additional_info = serializers.SerializerMethodField('get_additional_info')

#     def get_additional_info(self, instance ):


#         if  instance.is_staff:
#             info = Authorizer.objects.get(user = instance.id)
#             return AuthorizerSerializer(info).data
#         elif instance.gender ==None:
#             info = Director.objects.get(user = instance.id)
#             return DirectorSerializer(info).data
#         elif  instance.age:
#             info = Reviewer.objects.get(user = instance.id)
#             return ReviewerSerializer(info).data
#         else:
#             info = Cast.objects.get(user = instance.id)
#             return CastSerializer(info).data
        
#     class Meta:
#         model = User
#         fields = '__all__'
    


class SetNewPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)