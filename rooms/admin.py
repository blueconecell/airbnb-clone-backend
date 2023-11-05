from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
# admin action은 3개의 파라미터로 구성된다. 
# 1. 액션을 호출하는 클래스 
# 2. request객체
# 3. queryset 선택한 모든 객체를 반환
def reset_prices(modle_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "owner",
        "category",
        "rating",
        "created_at",

    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )
    search_fields = ("owner__username",)


    def total_amenities(self, room):
        return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
