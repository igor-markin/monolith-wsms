from django.contrib import admin
from .models import WebServer, WebServerRequest


@admin.register(WebServer)
class WebServerAdmin(admin.ModelAdmin):
    list_display = (
        'is_enabled',
        'name',
        'url',
        'status',
    )
    list_display_links = (
        'name',
        'url',
        'status',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'name',
        'url',
    )


@admin.register(WebServerRequest)
class WebServerRequestAdmin(admin.ModelAdmin):
    list_display = (
        'webserver',
        'started_at',
        'latency',
        'status_code',
        'status',
    )
    list_filter = (
        'webserver',
        'status_code',
        'status',
    )
