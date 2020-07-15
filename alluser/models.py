from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 用户扩展信息
class UserProfile(AbstractUser):
    # 用户
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    role_choices=(
        ('admin', '管理员'),
        ('collaborator','造梦者'),
        ('dreamer','实干者')
    )
    role = models.CharField(choices=role_choices,max_length=20, verbose_name="用户身份")
    phone = models.CharField(max_length=20, verbose_name=u'手机')
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True,verbose_name=u'头像')#avatar/%Y%m%d/头像地址
    bio = models.TextField(max_length=500, verbose_name=u'个人简介')
    datetime = models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
    isok = models.CharField(max_length=2)  # isok

    class Meta:
        verbose_name = '用户'  # 单数时显示内容
        verbose_name_plural = '用户'  # 复数时显示内容
    def __str__(self):
        return '{}'.format(self.user.username)  #admin显示