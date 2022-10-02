from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers import WebServerSerializer, WebServerRequestSerializer
from inspector.models import WebServer, WebServerRequest


class WebServerViewSet(viewsets.ModelViewSet):
    queryset = WebServer.objects.all()
    serializer_class = WebServerSerializer
    permission_classes = (AllowAny,)


class WebServerRequestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WebServerRequest.objects.all()
    serializer_class = WebServerRequestSerializer
    permission_classes = (AllowAny,)
