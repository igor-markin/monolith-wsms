from django.http import HttpResponse

from .models import WebServer


def test_view(request):
    return HttpResponse('ok')
