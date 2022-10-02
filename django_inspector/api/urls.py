from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import WebServerViewSet, WebServerRequestViewSet

router = DefaultRouter()
router.register(r'web_servers', WebServerViewSet, basename='web_server')
router.register(r'requests', WebServerRequestViewSet, basename='requests')
urlpatterns = router.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Web Servers Monitoring System API",
        default_version='v1',
        description=("Web Servers Monitoring System for "
                     "Monolith Backend Home Assignment"),
        terms_of_service="https://github.com/igor-markin/monolith-wsms",
        contact=openapi.Contact(email="9588604@gmail.com"),
        license=openapi.License(name="Apache-2.0 license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
