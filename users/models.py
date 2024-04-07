from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        "profile image", upload_to="users/profile", blank=True)
    short_description = models.TextField("Introduce", blank=True)
