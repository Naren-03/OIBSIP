from django.shortcuts import render
from django.http import HttpResponse
from . import utils
# Create your views here.

price = "00.00"
details = None


def home(request):
    utils.extract()
    drive = utils.carbrand()[0]
    engine = utils.carbrand()[1]
    fuel = utils.carbrand()[2]
    carbrand = utils.carbrand()[3]
    fuel_type = utils.carbrand()[4]
    asp_type = utils.carbrand()[5]
    

    
    if request.method=='POST':
        global get_cars
        global get_fuel_system 
        global get_engine 
        global get_drive
        global get_asp 
        global get_ftype
        global price
        global details 


        symboling = int(request.POST.get('symboling'))
        doornumber = int(request.POST.get('doornumber'))
        wheelbase = float(request.POST.get('wheelbase'))
        carlength = float(request.POST.get('carlength'))
        carwidth = float(request.POST.get('carwidth'))
        carheight = float(request.POST.get('carheight'))
        cylindernumber = int(request.POST.get('cylindernumber'))
        enginesize = int(request.POST.get('enginesize'))
        boreratio = float(request.POST.get('boreratio'))
        compressionratio = float(request.POST.get('compressionratio'))
        horsepower = int(request.POST.get('horsepower'))
        citympg = int(request.POST.get('citympg'))
        highwaympg = int(request.POST.get('highwaympg'))
        stroke = int(request.POST.get('stroke'))
        peakrpm = float(request.POST.get('peakrpm'))
        curbweight = float(request.POST.get('curbweight'))
        get_cars = request.POST.get('cars')
        get_fuel_system = request.POST.get('fuel_system')
        get_engine = request.POST.get('engine')
        get_drive = request.POST.get('drive')
        get_asp = request.POST.get('asp')
        get_ftype = request.POST.get('ftype')

        price = utils.predict_price(symboling, doornumber, wheelbase, carlength, carwidth, carheight, cylindernumber, enginesize, boreratio, stroke, compressionratio, horsepower, citympg, highwaympg, peakrpm, curbweight,get_ftype,get_asp,get_drive,get_engine,get_fuel_system,get_cars)

        details = [symboling, doornumber, wheelbase, carlength, carwidth, carheight, cylindernumber, enginesize, boreratio, stroke, compressionratio, horsepower, citympg, highwaympg, peakrpm, curbweight,get_ftype,get_asp,get_drive,get_engine,get_fuel_system,get_cars.upper()]
        print(price)
    params = {'drive':drive,'engine':engine,'fuel':fuel,'cars':carbrand,'fuel_type':fuel_type,'asp_type':asp_type,'Price':price,"Details":details}
    return render (request,"index.html",params)

