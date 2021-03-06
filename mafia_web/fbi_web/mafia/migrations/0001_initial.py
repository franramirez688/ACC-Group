# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MafiaEventsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imprisoned_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MafiaMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('labor_seniority', models.IntegerField(blank=True, default=0, null=True)),
                ('level', models.IntegerField(blank=True, default=0, null=True)),
                ('imprisoned', models.BooleanField(default=False)),
                ('promoted', models.BooleanField(default=False)),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='mafia.MafiaMember')),
            ],
        ),
    ]
