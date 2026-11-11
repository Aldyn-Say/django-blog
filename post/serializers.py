from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True) # Выводим инфу об авторе

    class Meta:
        model = Post
        fields = '__all__'

class PostWithAuthorIdSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author_id']