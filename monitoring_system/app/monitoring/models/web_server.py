from django.db import models


class WebServer(models.Model):
    class Status(models.TextChoices):
        HEALTHY = 'H', 'Healthy'
        UNHEALTHY = 'U', 'Unhealthy'

    is_enabled = models.BooleanField(
        verbose_name='Is enabled',
        help_text=('If enabled, the system will check '
                   'the status of the web server'),
        default=True,
    )
    name = models.CharField(
        verbose_name='Name',
        help_text='For example: My personal blog',
        max_length=100,
    )
    url = models.URLField(
        verbose_name='URL',
        help_text='For example: https://google.com',
    )
    status = models.CharField(
        verbose_name='Status',
        help_text='Default: healthy',
        max_length=1,
        choices=Status.choices,
        default=Status.HEALTHY,
    )

    class Meta:
        verbose_name = 'Web server'
        verbose_name_plural = 'Web servers'

    def __str__(self):
        return self.url

    @staticmethod
    def get_enabled_webservers():
        return WebServer.objects.filter(is_enabled=True)
