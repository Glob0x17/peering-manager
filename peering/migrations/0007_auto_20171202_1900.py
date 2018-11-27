# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0006_auto_20171017_1917")]

    operations = [
        migrations.AddField(
            model_name="autonomoussystem",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="communities",
            field=models.ManyToManyField(blank=True, to="peering.Community"),
        ),
    ]
