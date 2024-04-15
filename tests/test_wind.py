import pytest
from src.weather_api import wind


@pytest.mark.parametrize(
        "validationInput, validationExpected",
        [
            pytest.param(True, True, id="Array is filled"),
            pytest.param(False, True, id="Array is not filled")
        ]
)

def test_validateWindArray(validationInput, validationExpected):
    assert wind.validateWindArray(validationInput) == validationExpected

def test_getWindArray():
    windArray = wind.getWindArray()
    for i in range(24):
        assert windArray[i][0] in ["N", "NW", "W", "SW", "S", "SE", "E", "NE"]
        assert isinstance(windArray[i][1], int)
    
# fill wind array with mock data
@pytest.mark.parametrize(
    "direction, speed",
    [
        pytest.param("W", 10, id="Wind direction is West, speed is 10"),
        pytest.param("NW", 15, id="Wind direction is Northwest, speed is 15")
    ]
)

def test_fillWindArrayMocker(mocker, direction, speed):
    mocker.patch.object(wind.sensors, "readWindDirection", return_value=direction)
    mocker.patch.object(wind.sensors, "readWindSpeed", return_value=speed)
    wind.fillWindArray()
    for i in range(24):
        assert wind.windArray[i][0] == direction
        assert wind.windArray[i][1] == speed

# get wind array with mock data
@pytest.mark.parametrize(
    "direction, speed",
    [
        pytest.param("N", 5, id="North direction, speed 5"),
        pytest.param("NW", 10, id="Northwest direction, speed 10"),
        pytest.param("W", 15, id="West direction, speed 15"),
    ]
)

def test_getWindArrayMocker(mocker, direction, speed):
    mocker.patch.object(wind.sensors, "readWindDirection", return_value=direction)
    mocker.patch.object(wind.sensors, "readWindSpeed", return_value=speed)
    windArray = wind.getWindArray()
    for i in range(24):
        assert windArray[i][0] == direction
        assert windArray[i][1] == speed