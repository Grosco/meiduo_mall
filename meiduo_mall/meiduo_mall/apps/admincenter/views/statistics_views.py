from datetime import date

from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import OrderInfo

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
        count = User.objects.filter(orderinfo__create_time__gte=current_date).count()
        serialized = {
            'count': count,
            'date': current_date
        }
        return Response(serialized)
