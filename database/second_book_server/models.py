from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db import models
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password,university):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            user_nickname = username,
            university = university
        )
        user.set_password(password)
        user.save(using = self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    object = MyUserManager()
    register_time = models.DateTimeField('Register time',auto_now_add=True)
    user_nickname = models.CharField(max_length=30,default= "")
    university = models.CharField(max_length=30,default="")
    user_profile = models.TextField()
    USERNAME_FIELD = 'email'
