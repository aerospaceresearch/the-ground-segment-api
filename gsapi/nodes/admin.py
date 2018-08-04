from django.contrib import admin

from .models import Job, Node, Status, Upload


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('node', 'start', 'stop', 'description', 'default')


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
