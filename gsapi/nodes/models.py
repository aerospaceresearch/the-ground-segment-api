# coding: utf-8
import os.path
import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


class Node(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.TextField()
    node_type = models.CharField(max_length=20,
                                 choices=(('recording', 'recording'),
                                          ('processing', 'processing'),))
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=11, null=True, blank=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=11, null=True, blank=True)
    altitude = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return f"{self.owner} {self.name}"

    class Meta:
        ordering = ('name', )


class Status(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    status_code = models.CharField(max_length=20,
                                   choices=(('OK', 'OK'),
                                            ('maintenance', 'maintenance'),
                                            ('working', 'working'),))
    node_time_utc = models.DateTimeField()
    data = JSONField(default=dict)

    def __str__(self):
        return f"Status for {self.node}"

    class Meta:
        verbose_name_plural = 'Status'
