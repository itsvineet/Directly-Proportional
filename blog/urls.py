from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.home,name='home'), 
     path('signup/', views.SignUpView.as_view(), name='signup'),
     path('create-post/', views.CreatePostView.as_view(), name='create_post'),
     path('posts/', views.PostListView.as_view(), name='post_list'),
     path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
     path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
     path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='update_post'),
     path('posts/<int:pk>/comment/', views.create_comment, name='create_comment'),
     path('posts/<int:pk>/comment/delete/', views.delete_comment,name='delete_comment'),
     path('posts/<int:pk>/comment/approve/', views.approve_comment, name='approve_comment'),
     path('draft/', views.DraftListView.as_view(), name='draft'),
     path('draft/publish/<int:pk>/', views.post_publish, name='publish')
     

 ]