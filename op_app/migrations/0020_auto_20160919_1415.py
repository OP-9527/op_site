# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0019_appname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appname',
            options={},
        ),
        migrations.AddField(
            model_name='appname',
            name='remark',
            field=models.CharField(default='1', max_length=100, verbose_name='\u5907\u6ce8'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appname',
            name='war_path',
            field=models.CharField(default='1', max_length=200, verbose_name='\u5e94\u7528\u5305\u8def\u5f84'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appname',
            name='app_name',
            field=models.CharField(max_length=100, verbose_name='\u5e94\u7528\u5305\u540d'),
        ),
        migrations.AlterField(
            model_name='appname',
            name='app_type',
            field=models.CharField(max_length=50, verbose_name='\u5e94\u7528\u5305\u7c7b\u578b'),
        ),
    ]
