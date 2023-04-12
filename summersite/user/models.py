from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    wechat_id = models.CharField(
        max_length=20, 
        blank=False, 
        unique=True, 
        verbose_name='wechat ID',
        help_text="Your Wechat/Weixin ID used to contact Look4Tutor service",
    )
    is_tutor = models.BooleanField(
        default=False, 
        verbose_name='Tutor',
        help_text="Designates whether the user is a tutor",
    )
