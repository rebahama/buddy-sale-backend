from rest_framework import serializers
from . models import Post
from .models import MultipleImage
from favorites.models import Favorite


class MultipleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultipleImage
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    images = MultipleImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(max_length=10000, allow_empty_file=True, use_url=False,),write_only=True)
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

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            new_image = MultipleImage.objects.create(post=post, image=image)

        return post


    class Meta:
        model = Post
        fields = '__all__'
