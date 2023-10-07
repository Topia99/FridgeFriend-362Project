from django.contrib.auth.models import AbstractUser
from django.db import models

# Create a Abstract User model here
class User(AbstractUser):
    email = models.EmailField(unique=True)  # User's email has to be unique