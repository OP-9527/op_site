# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0010_auto_20160823_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='os',
            field=models.CharField(max_length=200, verbose_name='\u64cd\u4f5c\u7cfb\u7edf'),
        ),
    ]
