from django.urls import path
from .views import PostList, UserPostList, PostDetail, PostCreate, PostUpdate, PostDelete
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostList.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('post/new/', PostCreate.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
