from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class create_blog(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class Retrieve_Update_Destroy_blog(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
