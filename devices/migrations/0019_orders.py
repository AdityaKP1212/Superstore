# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0018_auto_20171121_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50, unique=True)),
                ('orderno', models.IntegerField(default=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Company')),
            ],
        ),
    ]
