from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer,DirectorSerializer,ReviewerSerializer,CastSerializer,AuthorizerSerializer,UserReadSerializer
from .models import Director,Authorizer,Reviewer,Cast
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@api_view(['GET'])
def directors(request):
    try:
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True) 
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
def casts(request):
    try:
        casts = Cast.objects.all()
        serializer = CastSerializer(directors, many=True) 
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
def authorizers(request):
    try:
        authorizers = Director.objects.all()
        serializer = AuthorizerSerializer(directors, many=True) 
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
def directorDetails(request,pk):
    try:
        if Director.objects.filter(id = pk).exists():
            director = Director.objects.get(pk = pk)
            serializer = DirectorSerializer(director)
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



@api_view(['GET'])
def castDetails(request,pk):
    try:
        if Cast.objects.filter(id = pk).exists():
            cast = Cast.objects.get(pk = pk)
            serializer = CastSerializer(cast)
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




@api_view(['GET'])
def authorizerDetails(request,pk):
    try:
        if Authorizer.objects.filter(id = pk).exists():
            authorizer = Authorizer.objects.get(pk = pk)
            serializer = AuthorizerSerializer(authorizer)
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




@api_view(['GET'])
def reviewerDetails(request,pk):
    try:
        if Reviewer.objects.filter(id = pk).exists():
            reviewer = Reviewer.objects.get(pk = pk)
            serializer = ReviewerSerializer(reviewer)
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
def directorCreate(request):
    try:
        payload = request.data
        serializer = DirectorSerializer(data=payload)

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
    



@api_view(['POST'])
def castCreate(request):
    try:
        payload = request.data
        serializer = CastSerializer(data=payload)

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
    



@api_view(['POST'])
def authorizerCreate(request):
    try:
        payload = request.data
        payload.is_staff = True
        serializer = AuthorizerSerializer(data=payload)

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
    



@api_view(['POST'])
def reviewerCreate(request):
    try:
        payload = request.data
        serializer = ReviewerSerializer(data=payload)

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
def directorUpdate(request,pk):
    try:
        if Director.objects.get(id=pk).exists():
            instance = Director.objects.get(pk=pk)
            serializer = DirectorSerializer(instance, data=request.data, partial=True)

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
               



@api_view(['PATCH'])
def castUpdate(request,pk):
    try:
        if Cast.objects.get(id=pk).exists():
            instance = Cast.objects.get(pk=pk)
            serializer = CastSerializer(instance, data=request.data, partial=True)

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
  


@api_view(['PATCH'])
def authorizerUpdate(request,pk):
    try:
        if Authorizer.objects.get(id=pk).exists():
            instance = Authorizer.objects.get(pk=pk)
            serializer = AuthorizerSerializer(instance, data=request.data, partial=True)

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
  



@api_view(['PATCH'])
def reviewerUpdate(request,pk):
    try:
        if Reviewer.objects.get(id=pk).exists():
            instance = Reviewer.objects.get(pk=pk)
            serializer = ReviewerSerializer(instance, data=request.data, partial=True)

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
def directorDelete(request,pk):
    try:
        if Director.objects.filter(id=pk).exists():
            instance = Director.objects.get(id=pk)
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




@api_view(['DELETE'])
def castDelete(request,pk):
    try:
        if Cast.objects.filter(id=pk).exists():
            instance = Cast.objects.get(id=pk)
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




@api_view(['DELETE'])
def authorizerDelete(request,pk):
    try:
        if Authorizer.objects.filter(id=pk).exists():
            instance = Authorizer.objects.get(id=pk)
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




@api_view(['DELETE'])
def reviewerDelete(request,pk):
    try:
        if Reviewer.objects.filter(id=pk).exists():
            instance = Reviewer.objects.get(id=pk)
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




@api_view(['POST'])
def logIn(request):
    try:
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            email = UserSerializer.validated_data.get('email')
            password = UserSerializer.validated_data.get('password')
            
            if not email or not password :
                return Response({'error': 'email and Password are required.'}, 
                    status=status.HTTP_400_BAD_REQUEST)
         
            instance = User.objects.get(email=email)
            print("after user fetch")
            if password == instance.password: 
                print("inside password")
                refresh = RefreshToken.for_user(instance)
                tokens = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    } 
                       
                serializer1 = UserReadSerializer(instance)
                
                return Response(
                    {'message': 'Login successful!',
                      'tokens': tokens,
                      'customer': serializer1.data}, 
                    status=status.HTTP_200_OK
                )             
            else:
                return Response(
                    {'error': 'Invalid password.'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
    except:

        return Response({'error': 'customer not found.'},status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def resetPassword(request):
    pass

