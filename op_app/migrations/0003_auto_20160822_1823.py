# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0002_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='remark',
            field=models.CharField(max_length=160, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AddField(
            model_name='server',
            name='server_group',
            field=models.CharField(default='test', max_length=100, verbose_name='\u670d\u52a1\u5668\u7ec4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='status',
            field=models.CharField(max_length=50, null=True, verbose_name='\u673a\u5668\u72b6\u6001'),
        ),
    ]
