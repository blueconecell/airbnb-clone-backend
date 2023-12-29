from django.urls import path
from .views import Perks, PerkDetial

urlpatterns = [
    path("perks/",Perks.as_view()),
    path("perks/<int:pk>",PerkDetial.as_view()),
    
]
