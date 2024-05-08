# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20141210_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstorystatus',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='is archived'),
            preserve_default=True,
        ),
    ]
