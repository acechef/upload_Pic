# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goup', '0002_dream_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='dream_id',
        ),
    ]
