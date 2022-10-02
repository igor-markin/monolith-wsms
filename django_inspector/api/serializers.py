from rest_framework import serializers

from inspector.models import WebServer, WebServerRequest


class WebServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebServer
        fields = (
            'id',
            'is_enabled',
            'name',
            'url',
            'status',
            'get_status_display',
        )


class WebServerRequestSerializer(serializers.ModelSerializer):
    web_server = WebServerSerializer()

    class Meta:
        model = WebServerRequest
        fields = (
            'id',
            'web_server',
            'started_at',
            'latency',
            'status_code',
            'status',
            'get_status_display',
        )
