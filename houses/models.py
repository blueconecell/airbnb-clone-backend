from django.db import models

# Create your models here.


# models.Model을 상속받아야 한다.
class House(models.Model):

    """Model Definitions for Houses"""

    # house라는 어플리케이션의 DB에 name은 CharField속성을 갖고, 최대길이는 140자이다.
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
