# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0017_tcpdump'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=500, verbose_name='url')),
                ('app_name', models.CharField(max_length=50, verbose_name='\u5e94\u7528\u540d\u79f0')),
            ],
        ),
    ]
