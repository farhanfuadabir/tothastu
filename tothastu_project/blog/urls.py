from django.urls import path
from .views import PostList, PostDetail
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]
