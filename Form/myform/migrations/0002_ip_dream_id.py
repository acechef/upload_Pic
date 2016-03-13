# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='dream_id',
            field=models.IntegerField(default=0),
        ),
    ]
