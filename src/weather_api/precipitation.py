# This is the precipitation module.
# It should only be called from the forecast.py module


from src.sensors import readSensors as sensors

precipitationArray = [[None, None] for _ in range(24)]
len_pre = len(precipitationArray)
isArrayFilled = False


def fillPrecipitationArray():
    for i in range(len_pre):
        precipitationArray[i][0] = sensors.readPrecipitationType()
        precipitationArray[i][1] = sensors.readPrecipitationAmount()


def validPrecipitationArray(arrayFilled):
    if not arrayFilled:
        fillPrecipitationArray()
        arrayFilled = True
    else:
        arrayFilled = True
    return arrayFilled


def getPrecipitationArray():
    validPrecipitationArray(isArrayFilled)
    return precipitationArray
