from rest_framework import serializers
from . models import Post
from favorites.models import Favorite


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    category_name = serializers.ReadOnlyField(source='category.title')
    city_name = serializers.ReadOnlyField(source='city.city')
    is_owner = serializers.SerializerMethodField()
    favorite_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_favorite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favorite = Favorite.objects.filter(
                owner=user, post=obj
            ).first()
            return favorite.id if favorite else None
        return None


    class Meta:
        model = Post
        fields = '__all__'