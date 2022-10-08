from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import constants


class UserViewPagination(PageNumberPagination):
    page_size = constants.UserViewPagSize
    page_query_param = 'page'
    max_page_size = constants.UserViewMaxPagSize
    page_size_query_param = 'pagesize'

    def get_paginated_response(self, data):
        serialized = {
            'count': self.page.paginator.count,  # 总数量
            'lists': data,  # 用户数据
            'page': self.page.number,  # 当前页数
            'pages': self.page.paginator.num_pages,  # 总页数
            'pagesize': self.page_size  # 后端指定的页容量
        }
        return Response(serialized)


class SpecsViewSetPagination(PageNumberPagination):
    pass
