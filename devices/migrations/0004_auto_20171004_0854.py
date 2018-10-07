# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_remove_xiaomi_model_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=15000)),
                ('ram', models.CharField(max_length=10)),
                ('battery', models.CharField(default='3000mah', max_length=10)),
                ('display', models.FloatField(default=5.0)),
                ('processor', models.CharField(default='snapdragon', max_length=50)),
                ('gpu', models.CharField(default='adreno', max_length=40)),
                ('stockrom', models.CharField(default='android', max_length=40)),
                ('album_logo', models.CharField(max_length=1000)),
                ('is_favorite', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Company')),
            ],
        ),
        migrations.AlterField(
            model_name='oneplus',
            name='price',
            field=models.IntegerField(default=15000),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='price',
            field=models.IntegerField(default=15000),
        ),
    ]
