# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordexpiry',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
