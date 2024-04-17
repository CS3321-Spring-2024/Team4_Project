# this is the module for the wind related weather functions
# it should only be called by the forecast.py module

from src.sensors import readSensors as sensors

windArray = [[None, None] for i in range(24)]
isArrayFilled = False


def fillWindArray():
    for i in range(len(windArray)):
        windArray[i][0] = sensors.readWindDirection()
        windArray[i][1] = sensors.readWindSpeed()


def validateWindArray(arrayFilled):
    if not arrayFilled:
        fillWindArray()
        arrayFilled = True
    else:
        arrayFilled = True
    return arrayFilled


def getWindArray():
    validateWindArray(isArrayFilled)
    return windArray
