# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 15:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAction",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("object_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "action",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "created"),
                            (2, "modified"),
                            (3, "deleted"),
                            (4, "imported"),
                        ]
                    ),
                ),
                ("message", models.TextField(blank=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-time"]},
        )
    ]
