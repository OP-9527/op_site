# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0021_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='Blog',
            name='author',
            field=models.CharField(default='root', max_length=50, verbose_name='\u4f5c\u8005'),
            preserve_default=False,
        ),
    ]
