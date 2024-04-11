# this module is used to calculate the air quality index based on the concentration of pollutants
# the pollutants are PM2.5, PM10, CO, NO2, SO2, O3


from src.sensors import readSensors as sensors

# [PM2.5, PM10, CO, NO2, SO2, O3]
# pollutantsArray[7][2] = Carbon Monoxide reading at 12Am
pollutantsArray = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]
# [particulates, aerosols, composite]

pollutantsCompositeArray = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
]

pollutantsInitialized = False


# Private functions
def buildPollutantsArray():
    for i in range(24):
        pollutantsArray[i][0] = sensors.readPMTwoPointFive()
        pollutantsArray[i][1] = sensors.readPMTen()
        pollutantsArray[i][2] = sensors.readCarbonMonoxide()
        pollutantsArray[i][3] = sensors.readNitrogenDioxide()
        pollutantsArray[i][4] = sensors.readSulfurDioxide()
        pollutantsArray[i][5] = sensors.readOzone()


def calculateCompositePollutants():
    for i in range(24):
        pollutantsCompositeArray[i][0] = (
            pollutantsArray[i][0] + pollutantsArray[i][1]
        ) / 2
        pollutantsCompositeArray[i][1] = (
            pollutantsArray[i][3] + pollutantsArray[i][4] + pollutantsArray[i][5]
        ) / 3
        pollutantsCompositeArray[i][2] = (
            pollutantsCompositeArray[i][0] + pollutantsCompositeArray[i][1]
        ) / 2


def initializePollutants():
    if not pollutantsInitialized:
        buildPollutantsArray()
        calculateCompositePollutants()
        pollutantsInitialized = True


# Public functions
def reinitializePollutants():
    buildPollutantsArray()
    calculateCompositePollutants()
    pollutantsInitialized = True


def getPollutantsArray():
    initializePollutants()
    return pollutantsArray


def getCompositePollutantsArray():
    initializePollutants()
    return pollutantsCompositeArray
