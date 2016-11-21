# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0023_auto_20161102_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigManage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(max_length=100, verbose_name='IP')),
                ('file_path', models.CharField(max_length=200, verbose_name='\u6587\u4ef6\u8def\u5f84')),
            ],
        ),
    ]
