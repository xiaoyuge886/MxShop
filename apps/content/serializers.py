from rest_framework import serializers

from .models import Content


#商品列表页

class ContentSerializer(serializers.ModelSerializer):
    #覆盖外键字段
    #images是数据库中设置的related_name="images"

    class Meta:
        model = Content
        fields = '__all__'
