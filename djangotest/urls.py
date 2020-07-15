"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.urls import path,include
from django.conf.urls import url

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from items.views import ItemInfoViewSet,PartInfoViewSet,ProblemInfoViewSet,AnswerInfoViewSet,index
from alluser.views import UserProfileViewSet
router = DefaultRouter()
#配置items的url
router.register('items',ItemInfoViewSet)
router.register('parts',PartInfoViewSet)
router.register('problems',ProblemInfoViewSet)
router.register('answers',AnswerInfoViewSet)
#配置allusers的url
router.register('Userprofiles',UserProfileViewSet)

# ItemInfo_list = ItemInfoViewSet.as_view({
#     'get': 'list',
# })
urlpatterns = [
    # path('api-token-auth/', views.obtain_auth_token),
    path("api/",include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('index/', index),
]

urlpatterns += [
    #drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    #jwt的认证接口
    # path('jwt-auth/',obtain_jwt_token)
    path('login/', obtain_jwt_token)

]
# APPEND_SLASH=False