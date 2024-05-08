# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

# Generated by Django 1.10.2 on 2016-10-26 11:34
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0054_auto_20160928_0540'),
    ]

    operations = [
        migrations.RunSQL(
            """
                ALTER TABLE "projects_projectmodulesconfig"
                   ALTER COLUMN "config"
                           TYPE jsonb
                          USING regexp_replace("config"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """,
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.RunSQL(
            """
                ALTER TABLE "projects_projecttemplate"
                   ALTER COLUMN "roles"
                           TYPE jsonb
                          USING regexp_replace("roles"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "default_options"
                           TYPE jsonb
                          USING regexp_replace("default_options"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "epic_statuses"
                           TYPE jsonb
                          USING regexp_replace("epic_statuses"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "us_statuses"
                           TYPE jsonb
                          USING regexp_replace("us_statuses"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "points"
                           TYPE jsonb
                          USING regexp_replace("points"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "task_statuses"
                           TYPE jsonb
                          USING regexp_replace("task_statuses"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "issue_statuses"
                           TYPE jsonb
                          USING regexp_replace("issue_statuses"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "issue_types"
                           TYPE jsonb
                          USING regexp_replace("issue_types"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "priorities"
                           TYPE jsonb
                          USING regexp_replace("priorities"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb,

                   ALTER COLUMN "severities"
                           TYPE jsonb
                          USING regexp_replace("severities"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """,
            reverse_sql=migrations.RunSQL.noop
        ),
    ]