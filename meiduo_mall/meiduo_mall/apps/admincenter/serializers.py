from django.contrib.auth import get_user_model

from rest_framework import serializers

from goods.models import GoodsVisitCount

User = get_user_model()


class GoodsVisitCountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta(object):
        model = GoodsVisitCount
        fields = ('count', 'category')


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'username', 'mobile', 'email')
