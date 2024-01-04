from django.utils import timezone

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Booking

class CreateRoomBookingSerializer(ModelSerializer):
    
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    
    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
                )
    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate(self, data):

        # 체크인 시간은 체크 아웃 시간보다 빨라야 한다.
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("Check in should be smaller than check out.")
        
    
        # 체크인 시간과 체크아웃 시간 사이에 또다른 booking이 존재하면 안된다.
        # 물론 체크인 또는 체크아웃 중 하나라도 걸쳐있는 booking 또한 존재하면 안된다.
        if Booking.objects.filter(
            check_in__lt=data['check_out'],
            check_out__gt=data['check_in']
        ).exists():
            raise serializers.ValidationError('Those (or some) of those dates are already taken.')

        return data
        



class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
                )