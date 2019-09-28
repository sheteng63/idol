from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=20,verbose_name=u'微信昵称')
    code = models.CharField(max_length=20,verbose_name=u'code')
    create_time = models.TimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.TimeField(auto_now=True, verbose_name=u'修改时间')
    is_active = models.BooleanField(default=True, verbose_name=u'状态')

class DateOrder(models.Model): #约会
    create_time = models.TimeField(auto_now_add=True, verbose_name=u'创建时间')
    modify_time = models.TimeField(auto_now=True, verbose_name=u'修改时间')
    applyUserId=models.ForeignKey(User,verbose_name=u'申请人',on_delete=models.CASCADE,related_name=u'申请人') #申请人
    acceptUserId=models.ForeignKey(User,verbose_name=u'接受人',on_delete=models.CASCADE,related_name=u'接受人') #接受方
    date_time_start = models.TimeField(verbose_name=u'开始时间')                   #时间
    applyMark=models.CharField(max_length=2,verbose_name=u'申请者评分')  #申请者评分
    acceptMark = models.CharField(max_length=2,verbose_name=u'接受方评分') #接受方评分
    share_type = models.CharField(max_length=2,verbose_name=u'分享的类型') #分享的类型 01仅参与方可见 02 分想给大家
    is_active = models.BooleanField(default=True, verbose_name=u'状态')

class DateEvent(models.Model): #事件
    create_time = models.TimeField(auto_now_add=True,verbose_name=u'创建时间')
    modify_time = models.TimeField(auto_now=True,verbose_name=u'修改时间')
    event_time = models.TimeField(verbose_name=u'约会时间')
    create_user= models.ForeignKey(User,verbose_name=u'创建人',on_delete=models.CASCADE) #创建人
    event_name = models.CharField(max_length=20,verbose_name='活动名称')  #活动名称
    event_describle = models.CharField(max_length=200,verbose_name=u'活动描述') #活动描述
    event_photo = models.ImageField(verbose_name=u'照片')              #图片
    dateOrder = models.ForeignKey(DateOrder,verbose_name=u'约会',on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name=u'状态')

class Comment(models.Model):
    name = models.CharField(max_length=20,default=u'佚名',verbose_name=u'姓名')
    content = models.TextField(verbose_name=u'内容')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    dateOrder = models.ForeignKey(DateOrder,verbose_name=u'约会',on_delete=models.CASCADE)
    writeUser = models.ForeignKey(User,verbose_name=u'评论人',on_delete=models.CASCADE,related_name=u'评论人')
    toUser = models.ForeignKey(User,verbose_name=u'被评论人',on_delete=models.CASCADE,related_name=u'被评论人') #to
    is_active = models.BooleanField(default=True,verbose_name=u'状态')
