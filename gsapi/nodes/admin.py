from django.contrib import admin

from .models import Node, Status


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'node_type', 'description')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('node', 'status_code', 'node_time_utc')
