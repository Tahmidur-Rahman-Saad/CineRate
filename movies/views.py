from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def some_view(request):
    return Response({
                'code': status.HTTP_200_OK,
                'response': "Data Received Successfully",
               
        })