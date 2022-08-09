from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='home'),
    path('blog/blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/bloggers/', views.AuthorListView.as_view(), name='author-list'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('blog/blogger/<int:pk>/', views.author_detail, name='author-detail'),
    path('blog/blogger/<int:pk>/my-profile', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('blog/<int:pk>/create', views.comment, name='comment'),
    path('blog/<int:pk>/delete', views.CommentPostDeleteView.as_view(), name='delete'),
    path('add-new-post/', views.PostCreateView.as_view(), name='new-post'),
    path('blog/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit-post'),
    path('blog/blogs/<int:pk>', views.hide_post, name='hide-post'),
    path('blog/post-detail/<int:pk>/', views.hide_comment, name='hide-comment'),
]