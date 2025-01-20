from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieSerializer,MusicSerializer,MovieDirectorCastSerializer
from .models import Music,Movie
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


# Create your views here.
@api_view(['GET'])
def movies(request):
    try:

        search_term = request.query_params.get('search_term',None)
        movies = Movie.objects.all().order_by('-release_date')
        #implement the search functions
        if search_term is not None and search_term != "":
            movies = movies.filter(Q(name__icontains = search_term) | Q(language__icontains = search_term) | Q(director__name__icontains = search_term
                                    ) | Q(casts__name__icontains = search_term))



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
    try:
        payload = request.data
        serializer = MovieSerializer(data=payload)

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
def movieUpdate(request,pk):
    try:
        if Movie.objects.get(id=pk).exists():
            rating = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(rating, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'response': "Data updated successfully",
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
            'response': "Data did not found"
        })
    except Exception as e:
        # Handle unexpected exceptions
        return Response({
            'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'response': "An unexpected error occurred",
            'error': str(e)
        })
               



@api_view(['DELETE'])
def movieDelete(request,pk):
    try:
        if Movie.objects.filter(id=pk).exists():
            instance = Movie.objects.get(id=pk)
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


