from .models import Content
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .filters import ContentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

from .serializers import ContentSerializer


class ContentPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 12
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


class ContentListViewSet(CacheResponseMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    list:
        商品列表，分页，搜索，过滤，排序
    retrieve:
        获取商品详情
    '''

    # authentication_classes = (TokenAuthentication,)
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    #这里必须要定义一个默认的排序,否则会报错
    queryset = Content.objects.all().order_by('id')
    # 分页
    pagination_class = ContentPagination
    #序列化
    serializer_class = ContentSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    #过滤
    filter_class = ContentFilter
    #搜索
    search_fields = ('id',)
    #排序
    ordering_fields = ('id', 'add_time')

    #商品点击数 + 1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
