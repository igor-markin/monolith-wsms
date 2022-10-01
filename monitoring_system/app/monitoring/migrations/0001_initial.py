# Generated by Django 4.1.1 on 2022-10-01 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='For example: My personal blog', max_length=100, verbose_name='Web server name')),
                ('url', models.URLField(help_text='For example: https://google.com', verbose_name='Web server URL')),
                ('status', models.CharField(choices=[('H', 'Healthy'), ('U', 'Unhealthy')], default='H', help_text='Default: healthy', max_length=1, verbose_name='Web server status')),
            ],
            options={
                'verbose_name': 'Web Server',
                'verbose_name_plural': 'Web Servers',
            },
        ),
        migrations.CreateModel(
            name='WebServerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(verbose_name='Request start time')),
                ('latency', models.TimeField(verbose_name='Request latency')),
                ('status_code', models.PositiveSmallIntegerField(verbose_name='Response status code')),
                ('status', models.CharField(choices=[('S', 'Success'), ('F', 'Failure')], default='S', max_length=1, verbose_name='Web server request status')),
                ('webserver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.webserver')),
            ],
            options={
                'verbose_name': 'Web server request',
                'verbose_name_plural': 'Web server requests',
            },
        ),
    ]