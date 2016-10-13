# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0018_appstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_type', models.CharField(max_length=50, verbose_name='\u5e94\u7528\u7c7b\u578b')),
                ('app_name', models.CharField(max_length=50, verbose_name='\u66f4\u65b0\u5305\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5e94\u7528\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u5e94\u7528\u4fe1\u606f\u7ba1\u7406',
            },
        ),
    ]
