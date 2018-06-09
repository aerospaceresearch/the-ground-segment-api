from rest_framework import decorators, mixins, viewsets

from .models import Node, Status
from .serializers import NodeSerializer, StatusSerializer
from .authentication import NodeOwnerPermission


class StatusViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Status.objects.none()
    serializer_class = StatusSerializer

    def create_status(self, request, node, *args, **kwargs):
        request.data['node'] = node.pk
        return super().create(request, *args, **kwargs)


class NodeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (NodeOwnerPermission,)
    serializer_class = NodeSerializer

    def get_queryset(self):
        return Node.objects.all()

    @decorators.action(methods=['POST'], url_path='status', url_name='status', detail=True)
    def status_create(self, request, *args, **kwargs):
        node = self.get_object()
        sv = StatusViewSet()
        sv.initial(request, *args, **kwargs)
        sv.request = request
        return sv.create_status(request, node, *args, **kwargs)
