from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from . import serializers
from . import models
from django.contrib.auth.models import User  
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timedelta
import jwt  
from django.db.models import Q

def generate_access_token(user):       
    payload ={
        'user_id' : user.id,
        'exp' : datetime.utcnow() + timedelta(days=5),  
        'iat' :  datetime.utcnow()                                  
    }    
    #token authentication
    access_token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    return access_token
    
class Signup(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.User.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
                      
            serializer.save(
                password=make_password(serializer.validated_data['password']),
            )
            return Response({'message': 'User signed up successfully'})
                                       
        else:
            return Response({'error': serializer.errors})
        
       
                
class Login(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data = request.data)   
        if serializer.is_valid(): 
            user_name = serializer.validated_data.get('username')
            pass_word = serializer.validated_data['password']      
            try:
                logged_user = models.User.objects.get(username=user_name)
            except Exception as e:  
                return Response({"message" : str(e)},)    
            password_check = check_password(pass_word, logged_user.password)
            if password_check :
                token = generate_access_token(logged_user)
                response = Response()
                response.set_cookie('access_token', value=token, httponly=True)
                response.data = {
                    'message' : 'login success',
                    'access_token' : token
                }
                return response
            return Response({'error' : 'Invalid username or password'})
        else:
            return Response({'message': serializer.initial_data})
        
    
class Create(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        try : 
            logged_user = models.BlogPost.objects.get(id=payload['user_id'])

            if not logged_user :
                return Response({'message' : 'only an Blogpost can create the post'})
        except Exception as e:
            return Response({'error' : str(e)})
        serializer = serializers.BlogPostSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save(author=logged_user)
            return Response({'message': 'The Author post has beeen upload successfully!'})
        else:
            return Response({'error':serializer.errors})
     
class Update(APIView):
    def put(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        try : 
            logged_user = models.BlogPost.objects.get(id=payload['user_id'])

            if not logged_user :
                return Response({'message' : 'only an Blogpost can update'})
        except Exception as e:
            return Response({'error' : str(e)})
        serializer = serializers.BlogPostSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save(author=logged_user)
            return Response({'message': 'The Author post has beeen upload successfully!'})
        else:
            return Response({'error':serializer.errors})
     