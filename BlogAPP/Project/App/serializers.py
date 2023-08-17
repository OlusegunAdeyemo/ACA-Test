from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.User
        fields = ('id', 'username' , 'firstname', 'email', 'age', 'password')
        read_only_fields = ('id',)

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.BlogPost
        fields = ('id', 'title' , 'content', 'creation_date', 'author')
        read_only_fields = ('id',)

