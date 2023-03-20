from django.urls import path
from .views import create_blog, Retrieve_Update_Destroy_blog

urlpatterns = [
    path('blogposts/', create_blog.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', Retrieve_Update_Destroy_blog.as_view(), name='blogpost-retrieve-update-destroy'),
]
