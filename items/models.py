from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class ItemInfo(models.Model):
    #创建项目表的字段
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=u"用户")
    title=models.CharField(max_length=100,verbose_name=u"标题",unique=True) #标题
    explain=models.TextField(max_length=500,verbose_name='说明')#说明
    details=models.TextField(max_length=500,verbose_name='项目细节')#项目细节
    datetime =models.DateTimeField(default=timezone.now,verbose_name='创建时间')#项目创建时间
    isok=models.CharField(max_length=2)#isok

    class Meta:
        verbose_name = '项目'  # 单数时显示内容
        verbose_name_plural = '项目'  # 复数时显示内容
    def __str__(self):
        return self.title #admin显示
        # return '%s-%s' %(self.user, self.title)

class PartInfo(models.Model):
    #创建角色表的字段
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(ItemInfo,on_delete=models.CASCADE,verbose_name=u"项目")
    name = models.CharField(max_length=50,verbose_name=u'角色名')  # 角色名
    skill = models.TextField(max_length=500,verbose_name=u'所需技能')  # 所需技能
    experience = models.TextField(max_length=500,verbose_name=u'所需经验')  # 所需经验
    requirement = models.TextField(max_length=500,verbose_name=u'其他要求')  # 其他要求
    datetime = models.DateTimeField(default=timezone.now,verbose_name=u"新建时间")
    isok = models.CharField(max_length=2)  # isok

    class Meta:
        verbose_name = u'项目角色'  # 单数时显示内容
        verbose_name_plural = u'项目角色'  # 复数时显示内容
    def __str__(self):
        return  self.name


class ProblemInfo(models.Model):
    #创建问题表的字段
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(ItemInfo,on_delete=models.CASCADE,verbose_name=u"项目")
    questioner  = models.CharField(max_length=50,verbose_name=u"提问者")  # 提问者
    problem  = models.CharField(max_length=500,verbose_name=u"问题")  # 问题
    datetime = models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
    isok=models.CharField(max_length=2)  # isok
    class Meta:
        verbose_name = '项目问题'  # 单数时显示内容
        verbose_name_plural = '项目问题'  # 复数时显示内容
    def __str__(self):
        return self.problem

class AnswerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(ProblemInfo,on_delete=models.CASCADE,verbose_name=u"问题")
    respondent= models.CharField(max_length=50,verbose_name=u"回答者") #回答者
    answer = models.TextField(max_length=500,verbose_name=u"答案")  # 答案
    datetime = models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
    isok = models.CharField(max_length=2)  # isok
    class Meta:
        verbose_name = u'项目答案'  # 单数时显示内容
        verbose_name_plural = u'项目答案'  # 复数时显示内容
    def __str__(self):
        return  self.respondent
