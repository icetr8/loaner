# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 06:43
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('due_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=1000)),
                ('loanee', models.CharField(default=b'admin', max_length=300)),
                ('payment', models.CharField(choices=[(b'MONTHLY', b'MONTHLY'), (b'SEMI-ANNUALLY', b'SEMI-ANNUALLY'), (b'ANUALLY', b'ANNUALLY')], default=b'MONTHLY', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]