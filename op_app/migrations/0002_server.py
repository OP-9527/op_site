# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=20, verbose_name='\u5382\u5546')),
                ('productname', models.CharField(max_length=30, verbose_name='\u670d\u52a1\u5668\u578b\u53f7')),
                ('service_tag', models.CharField(unique=True, max_length=80, verbose_name='\u5e8f\u5217\u53f7')),
                ('cpu_model', models.CharField(max_length=50, verbose_name='CPU\u578b\u53f7')),
                ('cpu_nums', models.PositiveSmallIntegerField(verbose_name='CPU\u7ebf\u7a0b\u6570')),
                ('cpu_groups', models.PositiveSmallIntegerField(verbose_name='CPU\u7269\u7406\u6838\u6570')),
                ('mem', models.CharField(max_length=100, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('disk', models.CharField(max_length=300, verbose_name='\u786c\u76d8\u5927\u5c0f')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('os', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('network_all', models.CharField(max_length=20, verbose_name='\u5168\u90e8\u7f51\u5361')),
                ('network_up', models.CharField(max_length=20, verbose_name='\u542f\u7528\u7f51\u5361')),
                ('idc_name', models.CharField(max_length=40, null=True, verbose_name='\u6240\u5c5e\u673a\u623f', blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u5668\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
    ]
