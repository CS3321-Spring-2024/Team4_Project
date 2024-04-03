# this is the module for the wind related weather functions
# it should only be called by the forecast.py module

# had to add the sensors directory to the path so that the readSensors module could be imported
import sys
sys.path.append('../sensors')
import readSensors as sensors

windArray = [[None, None] for i in range(24)]

def fillWindArray():
    for i in range(len(windArray)):
        windArray[i][0] = sensors.readWindDirection()
        windArray[i][1] = sensors.readWindSpeed()

def setWindArray():
    fillWindArray()

def getWindArray():
    return windArray