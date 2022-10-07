from rest_framework import serializers

from goods.models import GoodsVisitCount


class GoodsVisitCountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta(object):
        model = GoodsVisitCount
        fields = ('count', 'category')
