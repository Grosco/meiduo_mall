from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from admincenter.serializers import GoodsVisitCountSerializer
from goods.models import GoodsVisitCount

# Create your views here.

# 获取当前用户模型类
User = get_user_model()


class UserTotalCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        count = User.objects.all().count()
        serialized = {
            'count': count,
            'date': current_date
        }
        return Response(serialized)


class UserDayCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        count = User.objects.filter(date_joined__gte=current_date).count()
        serialized = {
            'count': count,
            'date': current_date
        }
        return Response(serialized)


class UserActiveCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        count = User.objects.filter(last_login__gte=current_date).count()
        serialized = {
            'count': count,
            'date': current_date
        }
        return Response(serialized)


class UserOrderCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        # SELECT COUNT(*) AS `__count` FROM `tb_users` INNER JOIN `tb_order_info` ON (`tb_users`.`id` = `tb_order_info`.`user_id`) WHERE `tb_order_info`.`create_time` >= '2022-10-07 16:00:00'
        count = User.objects.filter(orderinfo__create_time__gte=current_date).count()
        serialized = {
            'count': count,
            'date': current_date
        }
        return Response(serialized)


class UserMonthCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        start_date = current_date - timedelta(29)
        serialized = []
        for i in range(30):
            index_date = start_date + timedelta(i)
            next_date = start_date + timedelta(i + 1)
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=next_date).count()
            data_index_date = {
                'count': count,
                'date': index_date
            }
            serialized.append(data_index_date)
        return Response(serialized)


class GoodsDayView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        data = GoodsVisitCount.objects.filter(date=current_date)
        serialized = GoodsVisitCountSerializer(data, many=True)
        return Response(serialized.data)
