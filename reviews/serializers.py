from rest_framework.serializers import ModelSerializer

from users.serializer import TinyUserSerializer
from .models import Review


class ReviewSerializer(ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ("user","payload","rating",)