from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review

# SimpleListFilter를 상속받는다.
class WordFilter(admin.SimpleListFilter):
    # 필수 - 필터제목
    title="Filter by words!"
    # 필수 - URL에 뜨는 내용 'potato=어쩌구' 이렇게 URl에 나옴
    parameter_name="potato"
    # 필수 - 필터 내용이 어떤 것이 나와야하는지 Override되야하는 lookup method
    # 튜플 리스트를 반환해야한다.
    def lookups(self, request, model_admin):
        # 두번째 튜플요소를 화면에 보여준다.
        return [
            ("good", "Good"),
            ("oh", "Oh"),
            ("wow","Wow")
        ]
    # 필터를 거친 결과물을 보여주는 메소드
    def queryset(self, request, reviews):
        # request에 GET을 사용할 것이다.
        # 바뀐 url을 읽어서 값을 뽑아올 수도 있지만 self를 이용하여 값을 가져올 수 있다.
        word = self.value()
        if word:
            # 리뷰 내용물에 word와 같은 값을 뽑아준다.
            return reviews.filter(payload__contains = word)
        else:
            return reviews

# 3점미만은 bad, 3점 이상은 good로 나눠주는 필터
class good_or_bad(admin.SimpleListFilter):
    title = "3점미만 = bad, 3점이상 = good"
    parameter_name = "good_or_bad"
    def lookups(self, request, model_admin):
        return [
            ("good","good"),
            ("bad","bad"),
        ]
    def queryset(self, request, reviews):
        feel = self.value()
        if feel == 'good':
            return reviews.filter(rating__gte = 3)
        elif feel == 'bad':
            return reviews.filter(rating__lt = 3)
        else:
            return reviews
                    


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
        WordFilter,
        good_or_bad,
        "user__is_host",
        "room__amenities",
        "room__pet_friendly",
    )