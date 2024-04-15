import pytest
import src.weather_api.precipitation as precipitation

# test if the array is filled or not
@pytest.mark.parametrize(
        "validInput, validExpected",
        [
            pytest.param(True, True, id="filled Array"),
            pytest.param(False, True, id="not filled Array")
        ]
)

def test_validPrecipitationArray(validInput, validExpected):
    assert precipitation.validPrecipitationArray(validInput) == validExpected


# test to validate the behavior of getPrecipitationArray
def test_getPrecipitationArray():
    precipitationArray = precipitation.getPrecipitationArray()
    for i in range(24):
        assert precipitationArray[i][0] in ["rain", "snow"]
        assert isinstance(precipitationArray[i][1], int)



# test to mock filling the precipitation array
@pytest.mark.parametrize(
            "precipitationType, precipitationAmount",
    [
        pytest.param("rain", 5, id="Precipitation type is rain, amount is 5"),
        pytest.param("snow", 10, id="Precipitation type is snow, amount is 10")
    ]
)
def test_fillPrecipitationArrayMocker(mocker, precipitationType, precipitationAmount):
    mocker.patch.object(precipitation.sensors, "readPrecipitationType", return_value=precipitationType)
    mocker.patch.object(precipitation.sensors, "readPrecipitationAmount", return_value=precipitationAmount)
    precipitation.fillPrecipitationArray()
    for i in range(24):
        assert precipitation.precipitationArray[i][0] == precipitationType
        assert precipitation.precipitationArray[i][1] == precipitationAmount


