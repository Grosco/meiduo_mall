from django.contrib.auth import get_user_model

from rest_framework import serializers

from goods.models import GoodsVisitCount, SPUSpecification

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


class SPUSpecificationSerializer(serializers.ModelSerializer):
    # 关联嵌套返回spu表的商品名
    spu = serializers.StringRelatedField(read_only=True)
    # 返回关联spu的id值
    spu_id = serializers.IntegerField()

    class Meta(object):
        model = SPUSpecification
        fields = '__all__'
