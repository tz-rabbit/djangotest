from django.shortcuts import render

# Create your views here.
from alluser.models import UserProfile
from alluser.serializers import UserProfileSerializer
from  rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets,mixins

class UserProfilePagination(PageNumberPagination):
    page_size=10
class UserProfileViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    "用户列表页"
    queryset =UserProfile.objects.all()
    serializer_class =UserProfileSerializer
    pagination_class = UserProfilePagination