from django.shortcuts import render
from rest_framework import generics, filters
from .models import Post
from .serializer import PostSerializer
from buddysale_drf.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [
        'price'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetalier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    