from httpx import Auth
from rest_framework import serializers
from post.models import Post, Tag
from author.models import Author
from author.serializer import AuthorSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']
        

class PostSerializer(serializers.Serializer):
    author = AuthorSerializer()
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'
    