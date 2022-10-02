from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('test/', include('inspector.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
