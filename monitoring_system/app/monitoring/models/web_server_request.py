from django.db import models
import requests
from datetime import datetime



class WebServerRequest(models.Model):
    class Status(models.TextChoices):
        SUCCESS = 'S', 'Success'
        FAILURE = 'F', 'Failure'

    web_server = models.ForeignKey(
        to='monitoring.WebServer',
        on_delete=models.CASCADE,
    )
    started_at = models.DateTimeField(
        verbose_name='Start time',
    )
    latency = models.PositiveSmallIntegerField(
        verbose_name='Latency in seconds',
    )
    status_code = models.PositiveSmallIntegerField(
        verbose_name='Response status code',
    )
    status = models.CharField(
        verbose_name='Status',
        max_length=1,
        choices=Status.choices,
        default=Status.SUCCESS,
    )

    class Meta:
        verbose_name = 'Web server request'
        verbose_name_plural = 'Web server requests'

    def __str__(self):
        return f'{self.web_server.url} — {self.latency} — {self.status}'

    # @staticmethod
    # def check_web_server_status(web_server: WebServer):
    #     check_web_server_status.delay(web_server)
