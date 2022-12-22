from django.db import IntegrityError
from rest_framework import serializers
from favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = '__all__'

    def create(self, validated_data):
        """ The user can't like a post twice
            if the user likes a post twice
            then raise the error."""
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })