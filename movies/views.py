from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieSerializer,MusicSerializer,MovieDirectorCastSerializer
from .models import Music,Movie
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,Avg
from datetime import timedelta
from django.utils.timezone import now
from ratings.models import Rating


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
def ratingsSet(request,key):
    try:
        if Movie.objects.filter(id=key).exists():
            
            if Rating.objects.filter(movie__name=key).exists():
                ratings = Rating.objects.filter(movie__name = key).aggregate(Avg('rating'))
                movie = Movie.objects.get(pk = key) 
                movie.rating  = ratings

                if ratings < 5 :
                    movie.save()
                    serializer = MovieDirectorCastSerializer(movie)
                    return Response({
                        'code': status.HTTP_200_OK,
                        'response': "Data Set Successfully",
                        'data': serializer.data
                        })
                else:
                    return Response({
                        'code': status.HTTP_400_BAD_REQUEST,
                        'response': "Invalid Data"
                        })

            
            else:
                movie.rating =None
                movie.save()
                return Response({
                        'code': status.HTTP_204_NO_CONTENT,
                        'response': "Rating not found"
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
def movieTopRatingChecking(request,days,counts):
    try:
        days_ago = now() - timedelta(days=days)
        movies = Movie.objects.filter(created_at__gte=days_ago).order_by('-rating')
        if movies.count() >= counts:
            movies = movies.all()[:counts]
        serializer = MovieDirectorCastSerializer(movies)
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
def musicRecentReleaseChecking(request,days,counts):
    try:
        days_ago = now() - timedelta(days=days)
        musics = Music.objects.filter(created_at__gte=days_ago).order_by('-publish_date')
        if musics.count() >= counts:
            musics = musics.all()[:counts]
        serializer = MusicSerializer(movies)
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
def musics(request):
    try:

        search_term = request.query_params.get('search_term',None)
        musics = Music.objects.all().order_by('-publish_date')
        #implement the search functions
        if search_term is not None and search_term != "":
            musics = musics.filter(Q(name__icontains = search_term) | Q(singers__icontains = search_term) | Q(movie__name__icontains = search_term
                                    ) | Q(lyrics__icontains = search_term))



        serializer = MusicSerializer(movies, many=True) 
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




