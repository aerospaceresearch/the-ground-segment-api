import datetime

from rest_framework import decorators, generics, mixins, parsers, viewsets, response

from .models import Job, Node, Status, Upload
from .serializers import JobSerializer, NodeSerializer, StatusSerializer, UploadSerializer
from .authentication import NodeOwnerPermission

class JobViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    permission_classes = (NodeOwnerPermission,)
    queryset = Job.objects.none()
    serializer_class = JobSerializer

    def create_job(self, request, node, *args, **kwargs):
        self.check_object_permissions(request, node)
        request.data['node'] = node.pk
        return super().create(request, *args, **kwargs)

    def list(self, request, node, *args, **kwargs):
        self.check_object_permissions(request, node)
        self.queryset = Job.objects.filter(node=node)
        return super().list(request, *args, **kwargs)


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

    @decorators.action(methods=['GET'], url_path='jobs', url_name='jobs', detail=True)
    def jobs_list(self, request, *args, **kwargs):
        node = self.get_object()
        jv = JobViewSet()
        jv.initial(request, *args, **kwargs)
        jv.request = request
        return jv.list(request, node, *args, **kwargs)

    @decorators.action(methods=['POST'], url_path='job', url_name='job', detail=True)
    def job_create(self, request, *args, **kwargs):
        node = self.get_object()
        jv = JobViewSet()
        jv.initial(request, *args, **kwargs)
        jv.request = request
        return jv.create_job(request, node, *args, **kwargs)

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

    @decorators.action(detail=False)
    def coordinates(self, request, *args, **kwargs):
        nodes = Node.objects.all()
        # FIXME: build using a serializer
        _json = {
            "type": "FeatureCollection",
            "features": []
        }
        for node in nodes.exclude(latitude__isnull=True).exclude(longitude__isnull=True):
            status_node = node.status_set.exclude(status_code='maintenance').first()
            if status_node:
                node_time = status_node.node_time_utc
                node_time = node_time.replace(tzinfo=None)
                # active set to 15 minutes for now
                status = True if (datetime.datetime.utcnow() - node_time).total_seconds() < 15*60 else False
            else:
                status = False
            _json['features'].append(
                {
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            node.longitude,
                            node.latitude,
                            node.altitude
                        ]
                    },
                    "type": "Feature",
                    "properties": {
                        "name": node.name,
                        "popupContent": node.description,
                    },
                    "id": node.pk,
                    "status": status,
                })
        return response.Response(_json)
