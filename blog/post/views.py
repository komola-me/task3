from django.shortcuts import render
from post.serializer import PostSerializer
from rest_framework import generics
from post.models import Post

# Create your views here.

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.object.all()

    
class PopularPostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_popular=True)


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.object.all()
    lookup_field = 'id'

    