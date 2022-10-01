from django.db import models


class WebServer(models.Model):
    class WebServerStatus(models.TextChoices):
        HEALTHY = 'H', 'Healthy'
        UNHEALTHY = 'U', 'Unhealthy'

    name = models.CharField(
        verbose_name='Web server name',
        help_text='For example: My personal blog',
        max_length=100,
    )
    url = models.URLField(
        verbose_name='Web server URL',
        help_text='For example: https://google.com',
    )
    status = models.CharField(
        verbose_name='Web server status',
        help_text='Default: healthy',
        max_length=1,
        choices=WebServerStatus.choices,
        default=WebServerStatus.HEALTHY,
    )

    class Meta:
        verbose_name = 'Web Server'
        verbose_name_plural = 'Web Servers'

    def __str__(self):
        return f'{self.name} — {self.url} — {self.status}'