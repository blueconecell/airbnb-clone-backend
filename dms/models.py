from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """채팅방 모델 정의"""

    user = models.ManyToManyField("users.User")

    def __str__(self) -> str:
        return "Chatting Room"


class Message(CommonModel):
    """메시지 모델 정의"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    room = models.ForeignKey(
        "dms.ChattingRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} : {self.text}"
