from rest_framework import decorators, generics, mixins, parsers, viewsets

from .models import Node, Status, Upload
from .serializers import NodeSerializer, StatusSerializer, UploadSerializer
from .authentication import NodeOwnerPermission


class StatusViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Status.objects.none()
    serializer_class = StatusSerializer

    def create_status(self, request, node, *args, **kwargs):
        request.data['node'] = node.pk
        return super().create(request, *args, **kwargs)


class UploadViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Upload.objects.none()
    serializer_class = UploadSerializer

    def create_upload(self, request, node, *args, **kwargs):
        request.data['node'] = node.pk
        return super().create(request, *args, **kwargs)


class NodeViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (NodeOwnerPermission,)
    serializer_class = NodeSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Node.objects.filter(owner=self.request.user)
        return Node.objects.none()

    def get_object(self):
        qs = Node.objects.all()
        return generics.get_object_or_404(qs, pk=self.kwargs['pk'])

    @decorators.action(methods=['POST'], url_path='status', url_name='status', detail=True)
    def status_create(self, request, *args, **kwargs):
        node = self.get_object()
        sv = StatusViewSet()
        sv.initial(request, *args, **kwargs)
        sv.request = request
        return sv.create_status(request, node, *args, **kwargs)

    @decorators.action(methods=['POST'], url_path='upload', url_name='upload', detail=True,
                       parser_classes=(parsers.MultiPartParser, parsers.FormParser))
    def upload_create(self, request, *args, **kwargs):
        node = self.get_object()
        uv = UploadViewSet()
        uv.initial(request, *args, **kwargs)
        uv.request = request
        return uv.create_upload(request, node, *args, **kwargs)
