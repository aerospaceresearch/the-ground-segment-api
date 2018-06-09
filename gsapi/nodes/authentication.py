from rest_framework import permissions

from .models import Node


class NodeOwnerPermission(permissions.BasePermission):
    """Checks if authenticated user is owner of the node"""

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Node):
            return request.META.get('HTTP_AUTHORIZATION') == 'Token ' + obj.token
        return False
