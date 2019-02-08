from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
#     path('createpost/', views.CreatePost.as_viwe(), name='create_post'),
     path('posts/', views.PostListView.as_view(), name='post_list'),
     path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail')

 ]