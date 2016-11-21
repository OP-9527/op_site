# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0022_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostaccount',
            name='remark',
            field=models.CharField(max_length=160, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
