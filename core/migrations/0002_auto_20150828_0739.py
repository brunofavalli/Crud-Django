# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='cpf',
            field=models.CharField(max_length=14),
            preserve_default=True,
        ),
    ]
