from django.db import models

# Create your models here.


# models.Model을 상속받아야 한다.
class House(models.Model):

    """Model Definitions for Houses"""

    # house라는 어플리케이션의 DB에 name은 CharField속성을 갖고, 최대길이는 140자이다.
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price",
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets allowed?",
        default=True,
        help_text="Does this house allows pets?",
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
