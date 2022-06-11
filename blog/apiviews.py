from .serializers import postSerializers
from rest_framework import generics
from .models import post




class AllPostsViewApi(generics.ListCreateAPIView):
    queryset =post.objects.all()
    serializer_class = postSerializers





