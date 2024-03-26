import math as math
import sensorFakes as sensors
# the idea here is that to switch to real sensors we just change the library name
# and the rest of the code should work without change


def readPMTwoPointFive():
    dirtyValue = sensors.sensePMTwoPointFive()
    cleanValue = math.ceil(dirtyValue) # better to be too cautious about air quality
    return cleanValue

def readPMTen():
    dirtyValue = sensors.sensePMTen()
    cleanValue = math.ceil(dirtyValue)
    return cleanValue

def readSulfurDioxide():
    dirtyValue = sensors.senseSulfurDioxide()
    cleanValue = math.ceil(dirtyValue)
    return cleanValue

def readNitrogenDioxide():
    dirtyValue = sensors.senseNitrogenDioxide()
    cleanValue = math.ceil(dirtyValue)
    return cleanValue

def readOzone():
    dirtyValue = sensors.senseOzone()
    cleanValue = math.ceil(dirtyValue) 
    return cleanValue
