from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from .models import Post
from .serializer import PostSerializer
from buddysale_drf.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter,
                       DjangoFilterBackend]
    ordering_fields = [
        'price'
    ]
    search_fields = [
        'title',
        'content',
        'category__title',
        'city__city'
    ]

    filterset_fields = [
        'category',
        'city',
        'owner__profile',
        'favorite__owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetalier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
