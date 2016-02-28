# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='ip',
            field=models.ForeignKey(default=datetime.datetime(2016, 2, 28, 10, 23, 6, 8019, tzinfo=utc), to='goup.IP'),
            preserve_default=False,
        ),
    ]
