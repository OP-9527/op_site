# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0020_auto_20160919_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6587\u7ae0\u53d1\u5e03\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u6587\u7ae0\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
    ]
