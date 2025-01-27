from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer,DirectorSerializer,DirectorReadSerializer,ReviewerSerializer,ReviewerReadSerializer,CastSerializer,CastReadSerializer,AuthorizerSerializer,AuthorizerReadSerializer,UserReadSerializer,SetNewPasswordSerializer
from .models import Director,Authorizer,Reviewer,Cast
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.cache import cache 
from django.contrib.auth.hashers import make_password


# Create your views here.
@api_view(['GET'])
def directors(request):
    try:
        directors = Director.objects.all()
        serializer = DirectorReadSerializer(directors, many=True) 
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
        serializer = CastReadSerializer(directors, many=True) 
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
        serializer = AuthorizerReadSerializer(directors, many=True) 
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
            serializer = DirectorReadSerializer(director)
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
            serializer = CastReadSerializer(cast)
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
            serializer = AuthorizerReadSerializer(authorizer)
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
            serializer = ReviewerReadSerializer(reviewer)
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
        data = request.data
        username = data['email']+data['first_name']+ data['last_name']+data['date_of_birth']

        data1 ={
            'username': username,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email':data['email'],
            'password': data['password'],
            'is_staff' : False
        }

        data2 = {
            'date_of_birth' :data['date_of_birth'],
            'Nationality' : data['Nationality'],
            'image' : data['image']
        }
        serializer1 = UserSerializer(data=data1)
        serializer2 = DirectorSerializer(data=data2)


        if serializer1.is_valid():
            serializer1.save()
            user = User.objects.get(email=data1['email'])
            user.set_password(data['password'])
            user.save()
            if serializer2.is_valid():
                serializer2.save(user = user)
                return Response({
                'code': status.HTTP_200_OK,
                'message': 'Data added successfully.'
                })
            else:
                return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })

        else:    
            return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
            })
    



@api_view(['POST'])
def castCreate(request):
    try:
        data = request.data
        username = data['email'] + data['first_name']+ data['last_name']+data['date_of_birth']

        data1 ={
            'username': username,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email':data['email'],
            'password': data['password'],
            'is_staff' : False
        }

        data2 = {
            'date_of_birth' :data['date_of_birth'],
            'Nationality' : data['Nationality'],
            'image' : data['image'],
            'gender' : data['gender']
        }
        serializer1 = UserSerializer(data=data1)
        serializer2 = CastSerializer(data=data2)


        if serializer1.is_valid():
            serializer1.save()
            user = User.objects.get(email=data1['email'])
            user.set_password(data['password'])
            user.save()
            if serializer2.is_valid():
                serializer2.save(user = user)
                return Response({
                'code': status.HTTP_200_OK,
                'message': 'Data added successfully.'
                })
            else:
                return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })

        else:    
            return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
            })
    



@api_view(['POST'])
def authorizerCreate(request):
    try:
        data = request.data
        username = data['email'] + data['first_name']+ data['last_name']+data['date_of_birth']

        data1 ={
            'username': username,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email':data['email'],
            'password': data['password'],
            'is_staff' : True
        }

        data2 = {
            'phone' :data['phone'],
            'nid' : data['nid'],
            'image' : data['image']
        }
        serializer1 = UserSerializer(data=data1)
        serializer2 = AuthorizerSerializer(data=data2)


        if serializer1.is_valid():
            serializer1.save()
            user = User.objects.get(email=data1['email'])
            user.set_password(data['password'])
            user.save()
            if serializer2.is_valid():
                serializer2.save(user = user)
                return Response({
                'code': status.HTTP_200_OK,
                'message': 'Data added successfully.'
                })
            else:
                return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })

        else:    
            return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
            })
    



@api_view(['POST'])
def reviewerCreate(request):
    try:
        data = request.data
        username = data['email'] + data['first_name']+ data['last_name']+data['date_of_birth']

        data1 ={
            'username': username,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email':data['email'],
            'password': data['password'],
            'is_staff' : True
        }

        data2 = {
            'age' :data['age'],
            'gender' : data['gender'],
            'image' : data['image']
        }
        serializer1 = UserSerializer(data=data1)
        serializer2 = ReviewerSerializer(data=data2)


        if serializer1.is_valid():
            serializer1.save()
            user = User.objects.get(email=data1['email'])
            user.set_password(data['password'])
            user.save()
            if serializer2.is_valid():
                serializer2.save(user = user)
                return Response({
                'code': status.HTTP_200_OK,
                'message': 'Data added successfully.'
                })
            else:
                return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })

        else:    
            return Response({
                   'code': status.HTTP_400_BAD_REQUEST,
                   'errors': serializer2.errors
                })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
            })
    


@api_view(['PATCH'])
def directorUpdate(request,pk):
    try:
        if Director.objects.filter(pk=pk).first():
            instance = Director.objects.get(pk=pk)
            user = instance.user

            # Remove 'password' field from request data if present
            request_data = request.data.copy()
            if 'password' in request_data:
                request_data.pop('password')

            serializer1 = UserSerializer(user, data=request_data, partial=True)
            serializer2 = DirectorSerializer(instance, data=request_data, partial=True)


            if serializer1.is_valid():
                serializer1.save()
                user.save()
                if serializer2.is_valid():
                    serializer2.save(user = user)
                    return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Data Updated successfully.'
                    })
                else:
                    return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
                    })
    
            else:    
                return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
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
        if Cast.objects.filter(pk=pk).first():
            instance = Cast.objects.get(pk=pk)
            user = instance.user
            # Remove 'password' field from request data if present
            request_data = request.data.copy()
            if 'password' in request_data:
                request_data.pop('password')

            serializer1 = UserSerializer(user, data=request_data, partial=True)
            serializer2 = CastSerializer(instance, data=request_data, partial=True)


            if serializer1.is_valid():
                serializer1.save()
                user.save()
                if serializer2.is_valid():
                    serializer2.save(user = user)
                    return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Data Updated successfully.'
                    })
                else:
                    return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
                    })
    
            else:    
                return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
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
        if Authorizer.objects.filter(pk=pk).first():
            instance = Authorizer.objects.get(pk=pk)
            user = instance.user
            # Remove 'password' field from request data if present
            request_data = request.data.copy()
            if 'password' in request_data:
                request_data.pop('password')

            serializer1 = UserSerializer(user, data=request_data, partial=True)
            serializer2 = AuthorizerSerializer(instance, data=request_data, partial=True)


            if serializer1.is_valid():
                serializer1.save()
                user.save()
                if serializer2.is_valid():
                    serializer2.save(user = user)
                    return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Data Updated successfully.'
                    })
                else:
                    return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
                    })
    
            else:    
                return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
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
        if Authorizer.objects.filter(pk=pk).first():
            instance = Authorizer.objects.get(pk=pk)
            user = instance.user
            # Remove 'password' field from request data if present
            request_data = request.data.copy()
            if 'password' in request_data:
                request_data.pop('password')

            serializer1 = UserSerializer(user, data=request_data, partial=True)
            serializer2 = AuthorizerSerializer(instance, data=request_data, partial=True)


            if serializer1.is_valid():
                serializer1.save()
                user.save()
                if serializer2.is_valid():
                    serializer2.save(user = user)
                    return Response({
                    'code': status.HTTP_200_OK,
                    'message': 'Data Updated successfully.'
                    })
                else:
                    return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
                    })
    
            else:    
                return Response({
                       'code': status.HTTP_400_BAD_REQUEST,
                       'errors': serializer2.errors
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
def resetPasswordSendLink(request):
    try:
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            reset_token = get_random_string(50)
            send_mail(
                    "Password Reset",
                    f"Use this token to reset your password: {reset_token}",
                    "noreply@example.com",
                    [email],
                )
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Reset token sent to your email.",
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


@api_view(['POST'])
def resetPassword(request):
    try:
        serializer = SetNewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']
            user_id = cache.get(token)
            if not user_id:
                return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'response': 'Invalid or expired token.'
            })
            
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()

            # Invalidate the token after use
            cache.delete(token)
            return Response({
                'code': status.HTTP_200_OK,
                'response': "Password reset successfully.",
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



