from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    USER_TYPE_CHOICE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]

    user_type = models.CharField(choices=USER_TYPE_CHOICE, max_length=10)

    user_id = models.CharField(
        max_length=15,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        return self.username
    
