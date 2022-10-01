from django.contrib import admin
from .models import WebServer, WebServerRequest


@admin.register(WebServer)
class WebServerAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    search_fields = ('name', 'url')


@admin.register(WebServerRequest)
class WebServerRequestAdmin(admin.ModelAdmin):
    list_filter = ('webserver', 'status_code', 'status')
