from rest_framework import serializers

from .models import Job, Node, Status, Upload


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'node', 'start', 'stop', 'description',
                  'default', 'task')


class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Node
        fields = ('id', 'name', 'node_type')


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'node', 'status_code', 'node_time_utc', 'data', 'created')
        read_only_fields = ('created',)


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = ('id', 'node', 'upload', 'upload_type')
