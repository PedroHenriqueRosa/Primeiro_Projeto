from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    choices_cargo = (('V', 'Vendedor'),
                     ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )
