from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def movies(request):
    pass

@api_view(['GET'])
def movieDetails(request,pk):
    pass


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
def musicRecent(request):
    pass


