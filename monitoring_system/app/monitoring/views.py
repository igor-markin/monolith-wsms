from django.http import HttpResponse

from .tasks import check_web_server_status
from .models import WebServer


def test_view(request):
    web_servers = WebServer.get_enabled_webservers()
    if web_servers.count() < 1:
        return HttpResponse('no web servers')
    for web_server in web_servers:
        check_web_server_status.delay(web_server.id)
    return HttpResponse('ok')
