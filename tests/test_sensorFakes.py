import pytest
from src.sensors import sensorFakes


# sensePMTwoPointFive
def test_sensePMTwoPointFive():
    pm_value = sensorFakes.sensePMTwoPointFive()
    assert isinstance(pm_value, float)
    assert 0 <= pm_value <= 310  # Range considering contamination


# senseSulfurDioxide
def test_senseSulfurDioxide():
    sulfur_value = sensorFakes.senseSulfurDioxide()
    assert isinstance(sulfur_value, float)
    assert 0 <= sulfur_value <= 310


# senseWindDirection
@pytest.mark.parametrize(
        "wind_direction_input, expected_wind_direction",
        [
            (180, 180),
            (0, 0),
            (360, 360),
            (90,90),
        ],
        ids=["Input 180", "Input 0", "Input 360", "Input 90"]
)

def test_senseWindDirection(mocker, wind_direction_input, expected_wind_direction):
    mocker.patch("src.sensors.sensorFakes.rand.randint", return_value=wind_direction_input)
    result = sensorFakes.senseWindDirection()
    assert result == expected_wind_direction


# senseWindSpeed
def test_senseWindSpeed():
    wind_speed = sensorFakes.senseWindSpeed()
    assert isinstance(wind_speed, float)
    assert 0 <= wind_speed <= 25  # Wind speed range


# sensePrecipitationType
def test_sensePrecipitationType():
    precipitation_type = sensorFakes.sensePrecipitationType()
    assert precipitation_type in ["rain", "snow"]


# sensePrecipitationAmount
@pytest.mark.parametrize(
        "precipitation_amount_input, expected_precipitation_amount",
        [
            (5, 5),
            (0, 0),
            (10, 10),
        ],
        ids=["Input 5", "Input 0", "Input 10"]
)

def test_sensePrecipitationAmount(mocker, precipitation_amount_input, expected_precipitation_amount):
    mocker.patch("src.sensors.sensorFakes.rand.triangular", return_value=precipitation_amount_input)
    result = sensorFakes.sensePrecipitationAmount()
    assert result == expected_precipitation_amount
