# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0004_auto_20160822_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='remark',
            field=models.CharField(max_length=160, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
