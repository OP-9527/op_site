# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0011_auto_20160823_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appinfo',
            name='app_conf_path',
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='app_install_path',
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='app_log_path',
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='app_type',
        ),
        migrations.RemoveField(
            model_name='appinfo',
            name='ip',
        ),
        migrations.AddField(
            model_name='appinfo',
            name='app_ip',
            field=models.GenericIPAddressField(null=True, verbose_name='\u5e94\u7528IP', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='asset_number',
            field=models.CharField(max_length=100, null=True, verbose_name='\u8d44\u4ea7\u7f16\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='customer_code',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5ba2\u6237\u7f16\u7801', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='manage_ip',
            field=models.GenericIPAddressField(null=True, verbose_name='\u7ba1\u7406IP', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='port',
            field=models.CharField(max_length=100, null=True, verbose_name='\u7aef\u53e3', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='position',
            field=models.CharField(max_length=100, null=True, verbose_name='\u673a\u67dc', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='rel_ip',
            field=models.GenericIPAddressField(null=True, verbose_name='\u771f\u673aIP', blank=True),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='service_tag',
            field=models.CharField(max_length=100, null=True, verbose_name='\u670d\u52a1\u6807\u7b7e', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='app_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u90e8\u7f72\u5e94\u7528', blank=True),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='remark',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
