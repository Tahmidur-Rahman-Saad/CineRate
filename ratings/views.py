from django.shortcuts import render
from .serializers import RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Rating
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes
from django.db.models import Sum

# Create your views here.

@api_view(['GET'])
def ratings(request):
    try:
        if Rating.objects.all().exists():
            ratings = Rating.objects.all().order_by('-id')

            serializer = RatingSerializer(ratings, many=True)
            total_rating = Rating.objects.aggregate(total_sum=Sum('rating'))
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
                'total rating':total_rating,
                'data': serializer.data
            })
        else :
            return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'response': "Ratings does not found"
        })
    
    except Exception as e:
        return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not Valid",
                'error': str(e)
            })


@api_view(['GET'])
def ratingDetails(request,pk):
    try:
        if Rating.objects.filter(id=pk).exists():
            rating = Rating.objects.get(pk = pk)
            serializer = RatingSerializer(rating)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
                'data': serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'message': 'Record not found.'
            })
        
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })



@api_view(['POST'])
def ratingsCreate(request):
    try:
        payload = request.data
        serializer = RatingSerializer(data=payload)

        if serializer.is_valid():
            instance = serializer.save()

            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Data added successfully.',
                'data': serializer(instance).data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
            })
    


@api_view(['PATCH'])
def ratingsUpdate(request,pk):
    try:
        if Rating.objects.get(id=pk).exists():
            rating_data = request.data
            rating = Rating.objects.get(pk=pk)
            serializer = RatingSerializer(rating, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Rating updated successfully",
                    "data": serializer.data
                })
            
            else:
                return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data not valid",
                'error': serializer.errors
                })
    except ObjectDoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'response': "Ratings does not found"
        })
    except Exception as e:
        # Handle unexpected exceptions
        return Response({
            'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'response': "An unexpected error occurred",
            'error': str(e)
        })
               


@api_view(['DELETE'])
def ratingsDelete(request,pk):
    try:
        if Rating.objects.filter(id=pk).exists():
            instance = Rating.objects.get(id=pk)
            instance.delete()

            return Response({
                'code': status.HTTP_200_OK,
                'message': 'Deleted successfully.'
            })
        else:
            return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'message': 'Record not found.'
            })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
