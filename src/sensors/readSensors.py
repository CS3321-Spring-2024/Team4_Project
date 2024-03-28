import math as math
import sensorFakes as sensors

# the idea here is that to switch to real sensors we just change the library name
# and the rest of the code should work without change


def readPMTwoPointFive():
    dirtyValue = sensors.sensePMTwoPointFive()
    cleanValue = math.ceil(dirtyValue)  # better to be too cautious about air quality
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

def readWindDirection():
    dirtyValue = sensors.senseWindDirection()
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    index = math.floor((dirtyValue + 22.5) / 45) % 9
    cleanValue = directions[index]
    return cleanValue

def readWindSpeed():
    dirtyValue = sensors.senseWindSpeed()
    cleanValue = math.ceil(dirtyValue)
    return cleanValue


# precipitation
def readPrecipitationType():
    dirtyType = sensors.sensePrecipitationType()
    cleanType = dirtyType.strip().lower()
    return cleanType

def readPrecipitationAmount():
    dirtyAmount = sensors.sensePrecipitationAmount()
    cleanAmount = max(0, dirtyAmount)
    return cleanAmount
