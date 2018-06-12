from django.contrib import admin

from .models import Node, Status, Upload


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'node_type', 'description')
    readonly_fields = ['token']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('node', 'status_code', 'node_time_utc')


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('node', 'upload_type', 'upload')
