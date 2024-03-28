# This module is used to generate fake sensor data so that if real sensors were not available, we could still test the system.
import random as rand

# This zipcode will eventually have a post function to change it
zipCode = 83201  # Pocatello, ID
rand.seed(zipCode)


# Real pollutant values are not necessarily bounded, but we will assume that the values are between 0 and 300
# A triangular distibution just makes the numbers look more realistic
def sensePMTwoPointFive():
    dataContaminationAmount = rand.random()
    pmTwoPointFive = rand.triangular(0, 300, 10) + dataContaminationAmount
    return pmTwoPointFive


def sensePMTen():
    dataContaminationAmount = rand.random()
    pmTen = rand.triangular(0, 300, 10) + dataContaminationAmount
    return pmTen


def senseSulfurDioxide():
    dataContaminationAmount = rand.random()
    sulfurDioxide = rand.triangular(0, 300, 10) + dataContaminationAmount
    return sulfurDioxide


def senseNitrogenDioxide():
    dataContaminationAmount = rand.random()
    senseNitrogenDioxide = rand.triangular(0, 300, 10) + dataContaminationAmount
    return senseNitrogenDioxide


def senseOzone():
    dataContaminationAmount = rand.random()
    ozone = rand.triangular(0, 300, 10) + dataContaminationAmount
    return ozone

# Wind data
def senseWindDirection():
    windDirection = rand.randint(0, 360)
    return windDirection

def senseWindSpeed():
    windSpeed = rand.triangular(0, 20, 5)
    return windSpeed


# precipitation
def sensePrecipitationType():
    precipitation_types = ["rain", "snow"]
    precipitation_type = rand.choice(precipitation_types)
    return precipitation_type

def sensePrecipitationAmount():
    precipitation = rand.triangular(0, 10, 0)
    return precipitation