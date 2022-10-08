from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from admincenter.paginator import UserViewPagination
from admincenter.serializers import UserSerializer

# Create your views here.

# 获取当前用户模型类
User = get_user_model()


class UserView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    pagination_class = UserViewPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '' or keyword is None:
            return User.objects.all()
        return User.objects.filter(username=keyword)

    def get(self, request, *args, **kwargs):
        return super(UserView, self).get(self, request, *args, **kwargs)
