# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('content', models.TextField()),
                ('pic_name', models.CharField(max_length=30)),
                ('pic_path', models.FileField(upload_to=b'./upload/')),
                ('love_num', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('dream_id', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
