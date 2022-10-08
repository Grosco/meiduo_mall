from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from admincenter.paginator import  SpecsViewSetPagination
from admincenter.serializers import SPUSpecificationSerializer
from goods.models import SPUSpecification

# Create your views here.

# 获取当前用户模型类
User = get_user_model()


class SpecsViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecificationSerializer
    pagination_class = SpecsViewSetPagination


