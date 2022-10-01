from django.db import models


class WebServerRequest(models.Model):
    class WebServerRequestStatus(models.TextChoices):
        SUCCESS = 'S', 'Success'
        FAILURE = 'F', 'Failure'

    webserver = models.ForeignKey(
        to='monitoring.WebServer',
        on_delete=models.CASCADE,
    )
    started_at = models.DateTimeField(
        verbose_name='Request start time',
    )
    latency = models.TimeField(
        verbose_name='Request latency',
    )
    status_code = models.PositiveSmallIntegerField(
        verbose_name='Response status code',
    )
    status = models.CharField(
        verbose_name='Web server request status',
        max_length=1,
        choices=WebServerRequestStatus.choices,
        default=WebServerRequestStatus.SUCCESS,
    )

    class Meta:
        verbose_name = 'Web server request'
        verbose_name_plural = 'Web server requests'

    def __str__(self):
        return f'{self.webserver.url} — {self.latency} — {self.status}'
