# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0007_auto_20160823_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='add_time',
            field=models.CharField(max_length=50, verbose_name='\u4e0a\u67b6\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='server',
            name='idc',
            field=models.CharField(max_length=100, verbose_name='\u673a\u623f'),
        ),
        migrations.AlterField(
            model_name='server',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='server',
            name='manufacturer',
            field=models.CharField(max_length=20, verbose_name='\u5382\u5546'),
        ),
        migrations.AlterField(
            model_name='server',
            name='remark',
            field=models.CharField(max_length=160, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_group',
            field=models.CharField(max_length=100, verbose_name='\u670d\u52a1\u5668\u7ec4'),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_position',
            field=models.CharField(max_length=40, verbose_name='\u673a\u67b6\u4f4d'),
        ),
        migrations.AlterField(
            model_name='server',
            name='status',
            field=models.CharField(max_length=50, verbose_name='\u673a\u5668\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u4fe1\u606f\u83b7\u53d6\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='cpu_groups',
            field=models.PositiveSmallIntegerField(max_length=30, verbose_name='CPU\u7269\u7406\u6838\u6570'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='cpu_model',
            field=models.CharField(max_length=50, verbose_name='CPU\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='cpu_nums',
            field=models.PositiveSmallIntegerField(verbose_name='CPU\u7ebf\u7a0b\u6570'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='disk',
            field=models.CharField(max_length=300, verbose_name='\u786c\u76d8\u5927\u5c0f'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='hostname',
            field=models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='mem',
            field=models.CharField(max_length=100, verbose_name='\u5185\u5b58\u5927\u5c0f'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='network_all',
            field=models.CharField(max_length=20, verbose_name='\u7f51\u5361'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='network_up',
            field=models.CharField(max_length=20, verbose_name='\u5df2\u6fc0\u6d3b\u7f51\u5361'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='os',
            field=models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u7cfb\u7edf'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='productname',
            field=models.CharField(max_length=30, verbose_name='\u670d\u52a1\u5668\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='service_tag',
            field=models.CharField(max_length=80, verbose_name='\u5e8f\u5217\u53f7'),
        ),
    ]
