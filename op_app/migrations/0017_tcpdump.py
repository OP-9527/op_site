# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0016_hostaccount_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tcpdump',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=100, verbose_name='IP')),
                ('cmd', models.CharField(max_length=100, verbose_name='\u547d\u4ee4')),
            ],
        ),
    ]
