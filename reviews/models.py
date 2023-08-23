from django.db import models
from common.models import CommonModel

class Review(CommonModel):

    """ Review from user to a room or experience """

    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    room = models.ForeignKey('rooms.Room',null=True,blank=True,on_delete=models.SET_NULL,)
    experience = models.ForeignKey('experiences.Experience',null=True,blank=True,on_delete=models.CASCADE,)
    payload = models.TextField()
    rating = models.PositiveBigIntegerField()
    def __str__(self) -> str:
        return f'{self.room} -> {self.user} / {self.rating}★'