from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(db_column='CarId', primary_key=True)
    carModel = models.CharField(db_column='carModel', max_length=255)
    carMaker = models.CharField(db_column='carMaker', max_length=255)
    carManufactureYear = models.IntegerField(db_column='carManufactureYear')

    class Meta:
        db_table = 'Car'

class Refuel(models.Model):
    id = models.AutoField(db_column='RefuelId', primary_key=True)
    carId = models.ForeignKey(Car)
    refuelDate = models.DateTimeField(db_column='RefuelDate')
    refuelCost = models.FloatField(db_column='RefuelCost')
    refuelQty = models.FloatField(db_column='RefuelQty')
    note = models.TextField(db_column='Note', default=None)

    class Meta:
        db_table = 'Refuel'

class MeterInfo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    carId = models.ForeignKey(Car)
    date = models.DateField(db_column='fordate')
    isLowBattery = models.BooleanField(db_column='islowbattery')

    class Meta:
        db_table = 'meterInfo'
