# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0009_hostaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='cpu_groups',
            field=models.PositiveSmallIntegerField(verbose_name='CPU\u7269\u7406\u6838\u6570'),
        ),
    ]
