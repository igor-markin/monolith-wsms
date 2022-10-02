import os
from datetime import datetime

import requests
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def run_monitoring():
    from inspector.models import WebServer

    web_server_ids = WebServer.get_enabled_web_servers_ids()
    for web_server_id in web_server_ids:
        check_web_server_status.delay(web_server_id)


@shared_task
def check_web_server_status(web_server_id: int):
    from inspector.models import WebServer, WebServerRequest

    web_server = WebServer.objects.get(id=web_server_id)
    MAX_TIMEOUT = float(os.environ.get('MAX_TIMEOUT_IN_SECONDS', 60))
    started_at = datetime.now()

    try:
        r = requests.get(url=web_server.url, timeout=MAX_TIMEOUT)
        status_code = r.status_code
        latency = r.elapsed.seconds
    except requests.exceptions.Timeout:
        status_code = int(os.environ.get('ERROR_STATUS_CODE', 0))
        latency = MAX_TIMEOUT

    if status_code in range(200, 300) and latency < MAX_TIMEOUT:
        status = WebServerRequest.Status.SUCCESS
    else:
        status = WebServerRequest.Status.FAILURE

    WebServerRequest.objects.create(
        web_server=web_server,
        started_at=started_at,
        latency=latency,
        status_code=status_code,
        status=status,
    )
