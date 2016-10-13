# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('app_name', models.CharField(max_length=100)),
                ('app_type', models.CharField(max_length=50)),
                ('app_install_path', models.CharField(max_length=500, verbose_name='\u5e94\u7528\u90e8\u7f72\u76ee\u5f55')),
                ('app_conf_path', models.CharField(max_length=500)),
                ('app_log_path', models.CharField(max_length=500)),
                ('remark', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=40, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('idc_addr', models.CharField(max_length=400, verbose_name='\u673a\u623f\u5730\u5740')),
                ('idc_user_name', models.CharField(max_length=40, verbose_name='\u673a\u623f\u8054\u7cfb\u4eba')),
                ('idc_user_phone', models.CharField(max_length=40, verbose_name='\u673a\u623f\u8054\u7cfb\u4eba\u7535\u8bdd')),
                ('remark', models.CharField(max_length=100, verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]
