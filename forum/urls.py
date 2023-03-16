from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    # path('edit/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('my_posts/', views.MyPosts.as_view(), name='my_posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('upvote/<slug:slug>/', views.PostUpvote.as_view(), name='post_upvote'),
    path('downvote/<slug:slug>/', views.PostDownvote.as_view(), name='post_downvote'),
]
