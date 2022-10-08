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


class UserAddSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'username', 'mobile', 'email')
        extra_kwargs = {
            'username': {
                'max_length': 20,
                'min_length': 5
            },
            'password': {
                'max_length': 20,
                'min_length': 8,
                'write_only': True
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
