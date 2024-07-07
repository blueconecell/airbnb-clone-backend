from django.urls import path
from .views import PhotoDetail, UploadImg


urlpatterns = [
    path("photos/<int:pk>",PhotoDetail.as_view()),
    path("photos/upload/<int:pk>",UploadImg.as_view()),
]
