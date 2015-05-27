# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetService', '0002_asset_parentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='parentId',
        ),
        migrations.AddField(
            model_name='asset',
            name='parent',
            field=models.ForeignKey(related_name='children', to='assetService.Asset', null=True),
        ),
    ]
