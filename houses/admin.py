from django.contrib import admin
from .models import House


# decorator라고 부른다.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # 모든것을 상속받고 아무것도 하기 싫을 때 pass를 적는다.
    # pass

    # house에도 여러 항목을 보이게끔 만들어준다.
    list_display = [
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    ]
    list_filter = [
        "price_per_night",
        "pets_allowed",
    ]
    search_fields = ["address"]
