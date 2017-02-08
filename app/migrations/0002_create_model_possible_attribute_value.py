# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_create_model_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200, null=True, verbose_name='value')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Attribute', verbose_name='attribute')),
            ],
            options={
                'db_table': 'possible_attribute_values',
                'verbose_name': 'PossibleAttributeValue',
                'verbose_name_plural': 'PossibleAttributeValues',
            },
        ),
    ]
