# coding=utf-8
from rest_framework import routers
from django.conf.urls import include, url

from .views import NodeViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('nodes', NodeViewSet, base_name="node")


urlpatterns = [
    url(r'^v1/', include(router_v1.urls)),
]
