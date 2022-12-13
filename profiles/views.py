from django.shortcuts import render
from rest_framework import generics
from . models import Profile
from . serializer import ProfileSeralizer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSeralizer
