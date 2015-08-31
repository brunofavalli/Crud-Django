# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150828_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crud',
            name='sexo',
            field=models.CharField(max_length=9, choices=[(b'Feminino', b'Feminino'), (b'Masculino', b'Masculino')]),
            preserve_default=True,
        ),
    ]
