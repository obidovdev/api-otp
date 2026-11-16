from django.urls import path
from .views import PostList, PostCreateView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
]