from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('test/', include('monitoring.urls')),
    path('admin/', admin.site.urls),
]
