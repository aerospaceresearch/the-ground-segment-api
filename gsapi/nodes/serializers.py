from rest_framework import serializers

from .models import Node, Status, Upload


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'node', 'status_code', 'node_time_utc', 'data')


class NodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Node
        fields = ('id', 'name', 'node_type')


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = ('id', 'node', 'upload', 'upload_type')
