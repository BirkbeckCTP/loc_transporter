# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-10-10 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loc_transporter', '0002_auto_20220825_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalsrn',
            name='srn',
            field=models.CharField(help_text='Library of Congress SRN.', max_length=12, verbose_name='SRN'),
        ),
    ]
