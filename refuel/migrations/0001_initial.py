# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'CarId')),
                ('carModel', models.CharField(max_length=255, db_column=b'carModel')),
                ('carMaker', models.CharField(max_length=255, db_column=b'carMaker')),
                ('carManufactureYear', models.IntegerField(db_column=b'carManufactureYear')),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='Refuel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'RefuelId')),
                ('refuelDate', models.DateTimeField(db_column=b'RefuelDate')),
                ('refuelCost', models.FloatField(db_column=b'RefuelCost')),
                ('refuelQty', models.FloatField(db_column=b'RefuelQty')),
                ('note', models.TextField(db_column=b'Note')),
                ('carId', models.OneToOneField(to='refuel.Car')),
            ],
            options={
                'db_table': 'Refuel',
            },
        ),
    ]
