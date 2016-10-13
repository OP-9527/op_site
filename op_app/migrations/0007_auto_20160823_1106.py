# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_app', '0006_auto_20160823_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
