from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist

from .models import Room, Amenity

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("name","description",)


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(many=True,read_only=True)
    category = CategorySerializer(read_only=True)

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True, )
    # reviews = ReviewSerializer(many=True, read_only=True)

    def get_rating(self, room):
        return room.rating()
    def get_is_owner(self,room):
        request = self.context["request"]
        return room.owner == request.user
    def get_is_liked(self,room):
        request = self.context['request']
        return Wishlist.objects.filter(
            user=request.user,
            rooms__pk=room.pk
            ).exists()

    class Meta:
        model = Room
        fields = "__all__"




class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True, )

    def get_rating(self, room):
        return room.rating()
    def get_is_owner(self,room):
        request = self.context["request"]
        return room.owner == request.user
    class Meta:
        model = Room
        fields = ("pk","name","country","city","price","rating","is_owner","photos",)