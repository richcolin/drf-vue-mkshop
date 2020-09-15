import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name='shop_price', help_text="最低价格",lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    name=django_filters.CharFilter(name='name',lookup_expr='icontains')


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax','name']