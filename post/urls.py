from django.urls import path
from .views import *

urlpatterns = [
    path('posts', PostListAPIView.as_view(), name='post-list-create'),
    path('post/<int:pk>', PostDetailAPIView.as_view(), name='post-detail'),
    path('post/create', PostCreateAPIView.as_view(), name='post-create'),
    path('post/update/<int:pk>', PostUpdateAPIView.as_view(), name='post-update'),
    path('post/delete/<int:pk>', PostDeleteAPIView.as_view(), name='post-delete'),
]