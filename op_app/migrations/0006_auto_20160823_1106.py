# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0005_auto_20160822_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('productname', models.CharField(max_length=30, null=True, verbose_name='\u670d\u52a1\u5668\u578b\u53f7')),
                ('service_tag', models.CharField(max_length=80, unique=True, null=True, verbose_name='\u5e8f\u5217\u53f7')),
                ('cpu_model', models.CharField(max_length=50, null=True, verbose_name='CPU\u578b\u53f7')),
                ('cpu_nums', models.PositiveSmallIntegerField(null=True, verbose_name='CPU\u7ebf\u7a0b\u6570')),
                ('cpu_groups', models.PositiveSmallIntegerField(null=True, verbose_name='CPU\u7269\u7406\u6838\u6570')),
                ('mem', models.CharField(max_length=100, null=True, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('disk', models.CharField(max_length=300, null=True, verbose_name='\u786c\u76d8\u5927\u5c0f')),
                ('hostname', models.CharField(max_length=30, null=True, verbose_name='\u4e3b\u673a\u540d')),
                ('os', models.CharField(max_length=20, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('network_all', models.CharField(max_length=20, null=True, verbose_name='\u7f51\u5361')),
                ('network_up', models.CharField(max_length=20, null=True, verbose_name='\u5df2\u6fc0\u6d3b\u7f51\u5361')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='\u4fe1\u606f\u83b7\u53d6\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u8be6\u7ec6\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u5668\u8be6\u7ec6\u4fe1\u606f',
            },
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name': '\u670d\u52a1\u5668\u7ba1\u7406', 'verbose_name_plural': '\u670d\u52a1\u5668\u7ba1\u7406'},
        ),
        migrations.RemoveField(
            model_name='server',
            name='cpu_groups',
        ),
        migrations.RemoveField(
            model_name='server',
            name='cpu_model',
        ),
        migrations.RemoveField(
            model_name='server',
            name='cpu_nums',
        ),
        migrations.RemoveField(
            model_name='server',
            name='disk',
        ),
        migrations.RemoveField(
            model_name='server',
            name='hostname',
        ),
        migrations.RemoveField(
            model_name='server',
            name='idc_name',
        ),
        migrations.RemoveField(
            model_name='server',
            name='mem',
        ),
        migrations.RemoveField(
            model_name='server',
            name='network_all',
        ),
        migrations.RemoveField(
            model_name='server',
            name='network_up',
        ),
        migrations.RemoveField(
            model_name='server',
            name='os',
        ),
        migrations.RemoveField(
            model_name='server',
            name='productname',
        ),
        migrations.RemoveField(
            model_name='server',
            name='service_tag',
        ),
        migrations.AddField(
            model_name='server',
            name='add_time',
            field=models.CharField(max_length=50, null=True, verbose_name='\u4e0a\u67b6\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='server',
            name='idc',
            field=models.CharField(max_length=100, null=True, verbose_name='\u673a\u623f'),
        ),
        migrations.AddField(
            model_name='server',
            name='server_position',
            field=models.CharField(max_length=40, null=True, verbose_name='\u673a\u67b6\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
