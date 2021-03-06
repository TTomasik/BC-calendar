# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 09:07
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('destination', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.IntegerField()),
                ('date_of_entry', models.DateTimeField(default=django.utils.timezone.now)),
                ('color', colorful.fields.RGBColorField()),
                ('tour_calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Calendar')),
            ],
        ),
    ]
