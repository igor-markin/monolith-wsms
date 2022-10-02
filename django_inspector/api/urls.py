from api.views import WebServerViewSet, WebServerRequestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'web_servers', WebServerViewSet, basename='web_server')
router.register(r'requests', WebServerRequestViewSet, basename='requests')
urlpatterns = router.urls
