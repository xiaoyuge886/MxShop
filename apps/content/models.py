
from datetime import datetime
from django.db import models
from users.models import UserProfile



class Content(models.Model):
    """
    内容
    """
    TYPES = (
        (0, "原创"),
        (1, "评论"),
        (2, "转发"),
    )
    STATE = (
        (0, "删除"),
        (1, "正常"),
    )

    PERMIT = (
        (0, "私密"),
        (1, "好友可见"),
        (2, "公开"),
    )

    user_profile_id = models.IntegerField("用户id", null=False, blank=False)
    content = models.CharField("内容",max_length=140)
    types = models.IntegerField(choices=TYPES)
    state = models.IntegerField(choices=STATE)
    top = models.BooleanField(default=False)
    permit =  models.IntegerField(choices=STATE)
    media_url = models.CharField("媒体地址",max_length=140)
    publish_location = models.CharField("地理位置",max_length=140)
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{self.id}'


class ContentInteract(models.Model):
    """
    内容互动
    """
    content_id = models.IntegerField("内容id", null=False, blank=False)
    like = models.IntegerField('点赞数')
    content = models.IntegerField("评论数")
    tran = models.BooleanField('转发数')
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "内容互动数"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Tag(models.Model):

    tag_key = models.CharField('标签的key', max_length=40)
    tag_name = models.CharField('标签的key', max_length=40)

    class Meta:
        verbose_name = "内容标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

class ContentTag(models.Model):

    content_id = models.IntegerField("内容id", null=False, blank=False)
    tag_id = models.IntegerField("tag_id", null=False, blank=False)

    class Meta:
        verbose_name = "内容的内容标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id