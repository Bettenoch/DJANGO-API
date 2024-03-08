# Create your models here.
import uuid;
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
from core.abstract.models import AbstractManager, AbstractModel

class UserManager(BaseUserManager, AbstractManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('User must have a username')
        if password is None:
            raise TypeError('User must have a password')
        if email is None:
            raise TypeError('User must have an email')
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise TypeError('Superuser must have a password');
        if email is None:
            raise TypeError('Superuser must have an email');
        if username is None:
            raise TypeError('Superuser must have a username');
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
   
    username = models.CharField(max_length=255, db_index=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects  = UserManager()

    def __str__(self):
        return f"{self.email}"
    @property

    def name(self):
        return f"{self.first_name} {self.last_name}"
