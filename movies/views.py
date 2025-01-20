from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieSerializer,MusicSerializer,MovieDirectorCastSerializer
from .models import Music,Movie
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@api_view(['GET'])
def movies(request):
    try:
        movies = Movie.objects.all().order_by('-release_date')[:50]#show the latest 50 movies
        serializer = MovieSerializer(movies, many=True) 
        return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
                'data': serializer.data
            })
    
    except ObjectDoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'response': "Data did not found"
        })
    
    except Exception as e:
        return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'response': "Data did not Valid",
                'error': str(e)
            })



@api_view(['GET'])
def movieDetails(request,pk):
    try:
        if Movie.objects.filter(id = pk).exists():
            movie = Movie.objects.get(pk = pk)
            serializer = MovieDirectorCastSerializer(movie)
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
def movieCreate(request):
    pass

@api_view(['PATCH'])
def movieUpdate(request,pk):
    pass


@api_view(['DELETE'])
def movieDelete(request,pk):
    pass


@api_view(['GET'])
def movieSearch(request):
    pass


@api_view(['GET'])
def movieTopTenRatingLastWeek(request):
    pass



@api_view(['GET'])
def movieTopTenRatingLastMonth(request):
    pass



@api_view(['GET'])
def movieTopTenRatingLastYear(request):
    pass



@api_view(['GET'])
def movieSearchByLanguage(request,language):
    pass


@api_view(['GET'])
def musicRecentRelease(request):
    pass



@api_view(['GET'])
def musicForSelectedMovie(request):
    pass


