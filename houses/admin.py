from django.contrib import admin
from .models import House


# decorator라고 부른다.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # 모든것을 상속받고 아무것도 하기 싫을 때 pass를 적는다.
    pass
