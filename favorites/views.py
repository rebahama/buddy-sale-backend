from django.shortcuts import render
from rest_framework import generics, permissions
from buddysale_drf.permissions import IsOwnerOrReadOnly
from favorites.models import Favorite
from favorites.serializer import FavoriteSerializer


class FavoriteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Favorite.objects.all()