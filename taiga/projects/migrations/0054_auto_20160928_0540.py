# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

# Generated by Django 1.9.2 on 2016-09-28 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0053_auto_20160927_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='user order'),
        ),
        migrations.AlterField(
            model_name='projecttemplate',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='user order'),
        ),
    ]
