from rest_framework import serializers

from medias.serializers import PhotoSerializer

from .models import Perk,Experience

class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = ("name","details","explanation")

class ExperienceDetailSerialier(serializers.ModelSerializer):
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