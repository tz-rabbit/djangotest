
from rest_framework import serializers
from items.models import  ItemInfo,PartInfo,ProblemInfo,AnswerInfo
class ItemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        # fields = ['id', 'user_id', 'title', 'explain', 'details', 'datetime', 'isok']
        fields ="__all__"
class PartInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartInfo
        fields ="__all__"
class ProblemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemInfo
        fields ="__all__"
class AnswerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerInfo
        fields ="__all__"

