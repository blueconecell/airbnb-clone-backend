# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model

from django.db import models
from django.contrib.auth.models import AbstractUser

# models.Model은 처음부터 다 만든다는 뜻
# class User(models.Model):
#     pass


# 이미 만들어져있는데 처음부터 만드는 행위는 비효율적이기 때문에 상속받아서 만들자


class User(AbstractUser):
    # Overriding
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150)
    is_host = models.BooleanField()
