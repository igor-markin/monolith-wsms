import os
from datetime import datetime

import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import mail_admins
from django.utils import timezone
from requests.exceptions import Timeout, ConnectionError

from inspector.models import WebServer, WebServerRequest

logger = get_task_logger(__name__)

MAX_TIMEOUT_IN_SECONDS = float(os.environ['MAX_TIMEOUT_IN_SECONDS'])
SUCCESSFULL_HTTP_RESPONSES = range(200, 300)


@shared_task
def run_monitoring():
    web_server_ids = WebServer.get_enabled_web_servers_ids()
    for web_server_id in web_server_ids:
        print(web_server_id)
        check_web_server_status.delay(web_server_id)


@shared_task
def check_web_server_status(web_server_id: int):
    web_server = WebServer.objects.get(id=web_server_id)
    protocol = web_server.url.split(':')[0].lower()
    if protocol in ('http', 'https'):
        _check_http_web_server_status(web_server, timezone.now())


def _check_http_web_server_status(web_server: WebServer, started_at: datetime):
    try:
        r = requests.get(url=web_server.url, timeout=MAX_TIMEOUT_IN_SECONDS)
        status_code = r.status_code
        latency = r.elapsed.seconds
        status = _get_web_server_request_status(r)
    except (Timeout, ConnectionError):
        status_code = int(os.environ['ERROR_STATUS_CODE'])
        latency = MAX_TIMEOUT_IN_SECONDS
        status = WebServerRequest.Status.FAILURE

    WebServerRequest.objects.create(
        web_server=web_server,
        started_at=started_at,
        latency=latency,
        status_code=status_code,
        status=status,
    )

    _change_web_server_status(web_server)


def _get_web_server_request_status(response: requests.Response) -> str:
    if (response.status_code in SUCCESSFULL_HTTP_RESPONSES
            and response.elapsed.seconds < MAX_TIMEOUT_IN_SECONDS):
        return WebServerRequest.Status.SUCCESS
    return WebServerRequest.Status.FAILURE


def _change_web_server_status(web_server: WebServer):
    web_servers = WebServerRequest.objects.filter(id=web_server.id)[:5]
    failure = 0
    success = 0
    for server in web_servers:
        if server.status == WebServerRequest.Status.FAILURE:
            failure += 1
        if server.status == WebServerRequest.Status.SUCCESS:
            success += 1

    if success >= int(os.environ['MIN_SUCCESS_REQUEST_COUNT']):
        if web_server.status != WebServer.Status.HEALTHY:
            web_server.status = WebServer.Status.HEALTHY
    elif failure >= int(os.environ['MIN_FAILURE_REQUEST_COUNT']):
        if web_server.status != WebServer.Status.UNHEALTHY:
            web_server.status = WebServer.Status.UNHEALTHY
            _send_email_admins(web_server)


def _send_email_admins(web_server: WebServer):
    subject = f'New unhealthy web server: {web_server.name}'
    message = (
        f'{web_server.name}\n'
        f'{web_server.url}\n'
        f'{web_server.status}\n'
    )
    mail_admins(subject, message)
