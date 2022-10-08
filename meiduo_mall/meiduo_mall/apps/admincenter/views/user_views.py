from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from admincenter.paginator import UserViewPagination
from admincenter.serializers import UserSerializer, UserAddSerializer

# Create your views here.

# 获取当前用户模型类
User = get_user_model()


class UserView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    # serializer_class = UserSerializer
    pagination_class = UserViewPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserAddSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '' or keyword is None:
            return User.objects.all()
        return User.objects.filter(username=keyword)
