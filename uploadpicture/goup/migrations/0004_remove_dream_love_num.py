# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goup', '0003_remove_ip_dream_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dream',
            name='love_num',
        ),
    ]
