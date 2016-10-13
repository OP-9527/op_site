# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0014_auto_20160826_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='app_ip',
            field=models.CharField(max_length=100, verbose_name='\u5e94\u7528IP'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='manage_ip',
            field=models.CharField(max_length=100, verbose_name='\u7ba1\u7406IP'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='rel_ip',
            field=models.CharField(max_length=100, verbose_name='\u771f\u673aIP'),
        ),
    ]
