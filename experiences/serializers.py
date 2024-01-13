from rest_framework import serializers

from medias.serializers import PhotoSerializer
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer

from .models import Perk,Experience

class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"

class ExperienceDetailSerialier(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True, )
    
    def get_rating(self, experience):
        return experience.rating()
    def get_is_host(self,experience):
        request = self.context["request"]
        return experience.host == request.user

    class Meta:
        model = Experience
        fields = "__all__"


class ExperienceListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True, )
    
    def get_rating(self, experience):
        return experience.rating()
    def get_is_host(self,experience):
        request = self.context["request"]
        return experience.host == request.user

    class Meta:
        model = Experience
        fields = ("pk","name","country","city","price","rating","is_host","photos",)