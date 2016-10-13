# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0012_auto_20160824_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='app_ip',
            field=models.GenericIPAddressField(verbose_name='\u5e94\u7528IP'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='app_name',
            field=models.CharField(max_length=100, verbose_name='\u90e8\u7f72\u5e94\u7528'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='asset_number',
            field=models.CharField(max_length=100, verbose_name='\u8d44\u4ea7\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='customer_code',
            field=models.CharField(max_length=100, verbose_name='\u5ba2\u6237\u7f16\u7801'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='manage_ip',
            field=models.GenericIPAddressField(verbose_name='\u7ba1\u7406IP'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='port',
            field=models.CharField(max_length=100, verbose_name='\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='position',
            field=models.CharField(max_length=100, verbose_name='\u673a\u67dc'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='rel_ip',
            field=models.GenericIPAddressField(verbose_name='\u771f\u673aIP'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='remark',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='service_tag',
            field=models.CharField(max_length=100, verbose_name='\u670d\u52a1\u6807\u7b7e'),
        ),
    ]
