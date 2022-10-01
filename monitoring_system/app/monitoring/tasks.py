from time import sleep
from celery import shared_task

from .models import WebServerRequest, WebServer
from datetime import datetime
import requests


@shared_task()
def check_web_server_status(web_server_id: int):
    web_server = WebServer.objects.get(id=web_server_id)
    now = datetime.now()

    try:
        r = requests.get(url=web_server.url, timeout=60.0)
        status_code = r.status_code
        latency = r.elapsed.seconds
    except requests.exceptions.ConnectionError:
        status_code = 0
        latency = 0

    if 200 <= status_code < 300 and latency < 60:
        status = WebServerRequest.Status.SUCCESS
    else:
        status = WebServerRequest.Status.FAILURE

    WebServerRequest.objects.create(
        web_server=web_server,
        started_at=now,
        latency=latency,
        status_code=status_code,
        status=status,
    )
