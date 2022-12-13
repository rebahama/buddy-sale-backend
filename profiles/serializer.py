from rest_framework import serializers
from . models import Profile


class ProfileSeralizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = '__all__'