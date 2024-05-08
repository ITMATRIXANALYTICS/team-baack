# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

# Generated by Django 1.11.2 on 2018-10-22 16:24
from __future__ import unicode_literals

import django.core.serializers.json
from django.db import migrations, models
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0012_auto_20161201_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='epiccustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='issuecustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='taskcustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='userstorycustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AlterField(
            model_name='epiccustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='issuecustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='taskcustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='userstorycustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
    ]
