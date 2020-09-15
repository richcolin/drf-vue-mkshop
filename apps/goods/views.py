
from .serializers import GoodsSerializer

from .models import Goods
from rest_framework import mixins
from .filters import GoodsFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    '''
    ceshiyixia
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class=GoodsFilter