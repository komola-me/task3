from django.urls import path, include
from post.views import PostListView, PopularPostListView, PostDetailView

urlpatterns = [
    path('post/', PostListView.as_view()),
    path('post/<int:id>', PostDetailView.as_view()),
    path('post/popular/', PopularPostListView.as_view()),
]
