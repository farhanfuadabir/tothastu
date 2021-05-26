from django.urls import path
from .views import PostList
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    # path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
