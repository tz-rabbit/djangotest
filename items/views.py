from django.shortcuts import render
from items.models import ItemInfo,PartInfo,ProblemInfo,AnswerInfo
from  rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt #跨域

# Create your views here.
from rest_framework import viewsets,mixins
from items.serializers import ItemInfoSerializer,PartInfoSerializer,ProblemInfoSerializer,AnswerInfoSerializer


class ItemInfoPagination(PageNumberPagination):
    page_size=10


class ItemInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    "项目列表页"
    queryset =ItemInfo.objects.all()
    serializer_class =ItemInfoSerializer
    pagination_class = ItemInfoPagination


class PartInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    "角色列表页"
    queryset =PartInfo.objects.all()
    serializer_class =PartInfoSerializer



class ProblemInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    "角色列表页"
    queryset =ProblemInfo.objects.all()
    serializer_class =ProblemInfoSerializer
class AnswerInfoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    "角色列表页"
    queryset =AnswerInfo.objects.all()
    serializer_class =AnswerInfoSerializer

@csrf_exempt
def index(request):
    return render(request,"test/apitest.html")
