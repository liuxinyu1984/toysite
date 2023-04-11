from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    wechat_id = models.CharField(max_length=20, blank=False, unique=True)
