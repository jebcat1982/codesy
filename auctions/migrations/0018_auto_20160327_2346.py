# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_payout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payout',
            name='bid',
        ),
        migrations.AddField(
            model_name='payout',
            name='claim',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='payouts', to='auctions.Claim'),
            preserve_default=False,
        ),
    ]