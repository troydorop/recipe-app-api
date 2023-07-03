"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class User(AbstractBaseUser, PermissionsMixin):
        """User in the system."""
        email = models.EmailFeild(max_length=255, uniqrue=True)
        name = models.Charfield(max_length=255)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        USERNAME_FIELD = 'email'