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


class UserView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = date.today()
        count = User.objects.all().count()
        serialized = {
            'count': count,
            'date': current_date
        }
        return Response(serialized)


