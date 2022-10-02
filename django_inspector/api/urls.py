from api.views import WebServerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'web_servers', WebServerViewSet, basename='web_server')
urlpatterns = router.urls
