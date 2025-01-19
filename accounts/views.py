from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def directors(request):
    pass


@api_view(['GET'])
def casts(request):
    pass


@api_view(['GET'])
def authorizers(request):
    pass

@api_view(['GET'])
def directorDetails(request,pk):
    pass

@api_view(['GET'])
def castDetails(request,pk):
    pass


@api_view(['GET'])
def authorizerDetails(request,pk):
    pass


@api_view(['GET'])
def reviewerDetails(request,pk):
    pass


@api_view(['POST'])
def directorCreate(request):
    pass


@api_view(['POST'])
def castCreate(request):
    pass


@api_view(['POST'])
def authorizerCreate(request):
    pass


@api_view(['POST'])
def reviewerCreate(request):
    pass

@api_view(['PATCH'])
def directorUpdate(request,pk):
    pass


@api_view(['PATCH'])
def castUpdate(request,pk):
    pass


@api_view(['PATCH'])
def authorizerUpdate(request,pk):
    pass


@api_view(['PATCH'])
def reviewerUpdate(request,pk):
    pass

@api_view(['DELETE'])
def directorDelete(request,pk):
    pass


@api_view(['DELETE'])
def castDelete(request,pk):
    pass


@api_view(['DELETE'])
def authorizerDelete(request,pk):
    pass


@api_view(['DELETE'])
def reviewerDelete(request,pk):
    pass


@api_view(['POST'])
def logIn(request):
    pass


@api_view(['POST'])
def resetPassword(request):
    pass

