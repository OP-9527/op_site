# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0015_auto_20160826_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostaccount',
            name='remark',
            field=models.CharField(default='test', max_length=160, verbose_name='\u5907\u6ce8'),
            preserve_default=False,
        ),
    ]
