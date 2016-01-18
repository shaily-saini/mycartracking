from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest
import datetime
import json
from models import Car, Refuel, MeterInfo

def welcome_page(request):
    return render(request, 'welcome_page.html', {})

def car_page(request):
    cars_queryset = Car.objects.all().values('id', 'carModel', 'carMaker', 'carManufactureYear')
    cars_json = json.dumps(list(cars_queryset), cls=DjangoJSONEncoder)
    return render(request, 'car.html', {'cars': json.loads(cars_json)})

def addNewCar(request):
    try:
        model = request.GET.get('model')
        maker = request.GET.get('maker')
        manufYear = request.GET.get('manuf_year')
        car = Car(carModel=model, carMaker=maker, carManufactureYear=manufYear)
        car.save()
        info = {}
        info['success'] = True
        return HttpResponse(json.dumps(info), content_type="application/json")
    except Exception as e:
        err = {}
        err['success'] = False
        err['message'] = str(e.message) + str(e)
        return HttpResponseBadRequest(json.dumps(err), content_type="application/json")

def get_refuel_view(request):
    cars = Car.objects.all()
    refuel_json = {}
    meter_json = {}
    for car in cars:
        if car.refuel_set.all():
            refuel_json[car.id] = json.dumps(list(car.refuel_set.all().values('id', 'refuelDate', 'refuelCost', 'refuelQty', 'note')), cls=DjangoJSONEncoder)
        if car.meterinfo_set.all():
            meter_json[car.id] = json.dumps(list(car.meterinfo_set.all().values('id', 'date', 'isLowBattery')), cls=DjangoJSONEncoder)
    cars_queryset = Car.objects.all().values('id', 'carModel', 'carMaker')
    cars_json = json.dumps(list(cars_queryset), cls=DjangoJSONEncoder)
    return render(request, 'refuel.html', {'cars': cars_json,
                                           'cars_json': json.loads(cars_json), 'refuel': json.dumps(refuel_json),
                                           'meter': json.dumps(meter_json)})

def refill_car(request):
    try:
        car = request.GET.get('car')
        cost = request.GET.get('cost')
        qty = request.GET.get('qty')
        fmt = '%d-%m-%Y'
        date = datetime.datetime.strptime(request.GET.get('date'), fmt).date()
        refuel = Refuel(carId_id=car, refuelDate=date, refuelCost=cost, refuelQty=qty, note='')
        refuel.save()
        print refuel
        info = {}
        info['success'] = True
        return HttpResponse(json.dumps(info), content_type="application/json")
    except Exception as e:
        print str(e.message)
        err = {}
        err['success'] = False
        err['message'] = str(e.message) + str(e)
        return HttpResponseBadRequest(json.dumps(err), content_type="application/json")

def unmark_low_battery(request):
    try:
        fmt = '%d-%m-%Y'
        fordate = datetime.datetime.strptime(request.GET.get('date'), fmt).date()
        carId = request.GET.get('car')
        info = MeterInfo.objects.filter(carId=carId, date=fordate)
        if info:
            info = info[0]
            if info.isLowBattery == True:
                info.isLowBattery = False
        info.save()
        info = {}
        info['success'] = True
        return HttpResponse(json.dumps(info), content_type="application/json")
    except Exception as e:
        err = {}
        err['success'] = False
        err['message'] = str(e.message) + str(e)
        return HttpResponseBadRequest(json.dumps(err), content_type="application/json")

def mark_low_battery(request):
    try:
        fmt = '%d-%m-%Y'
        fordate = datetime.datetime.strptime(request.GET.get('date'), fmt).date()
        carId = request.GET.get('car')
        info = MeterInfo.objects.filter(carId_id=carId, date=fordate)
        if not info:
            info = MeterInfo(carId_id=carId, date=fordate, isLowBattery=True)
        else:
            info = info[0]
            if info.isLowBattery == False:
                info.isLowBattery = True
        info.save()
        info = {}
        info['success'] = True
        return HttpResponse(json.dumps(info), content_type="application/json")
    except Exception as e:
        err = {}
        err['success'] = False
        err['message'] = str(e.message) + str(e)
        return HttpResponseBadRequest(json.dumps(err), content_type="application/json")
