import pytest
from src.weather_api import airQualityIndex


@pytest.mark.parametrize(
    "pollutant",
    [
        pytest.param(0, id="Zeros"),
        pytest.param(1.1, id="Floats"),
    ],
)
def test_buildPollutantsArray(mocker, pollutant):
    mocker.patch.object(
        airQualityIndex.sensors, "readPMTwoPointFive", return_value=pollutant
    )
    mocker.patch.object(airQualityIndex.sensors, "readPMTen", return_value=pollutant)
    mocker.patch.object(
        airQualityIndex.sensors, "readCarbonMonoxide", return_value=pollutant
    )
    mocker.patch.object(
        airQualityIndex.sensors, "readNitrogenDioxide", return_value=pollutant
    )
    mocker.patch.object(
        airQualityIndex.sensors, "readSulfurDioxide", return_value=pollutant
    )
    mocker.patch.object(airQualityIndex.sensors, "readOzone", return_value=pollutant)

    airQualityIndex.buildPollutantsArray()

    for i in range(24):
        for j in range(6):
            assert airQualityIndex.pollutantsArray[i][j] == pollutant


@pytest.mark.parametrize(
    "first_pollutant",
    "second_pollutant",
    "expected_result",
    [
        pytest.param(0, 0, 0, id="Zeros"),
        pytest.param(1.1, 1.1, 1.1, id="Floats"),
        pytest.param(20, 40.1, 30.05, id="MixedVals"),
    ],
)
def test_calculateCompositePollutants(
    first_pollutant,
    second_pollutant,
    expected_result,
):
    for i in range(24):
        airQualityIndex.pollutantsArray[i][0] = first_pollutant
        airQualityIndex.pollutantsArray[i][1] = first_pollutant
        airQualityIndex.pollutantsArray[i][2] = second_pollutant
        airQualityIndex.pollutantsArray[i][3] = second_pollutant
        airQualityIndex.pollutantsArray[i][4] = second_pollutant
        airQualityIndex.pollutantsArray[i][5] = second_pollutant

    airQualityIndex.calculateCompositePollutants()
    for i in range(24):
        assert airQualityIndex.compositePollutantsArray[i][0] == first_pollutant
        assert airQualityIndex.compositePollutantsArray[i][1] == second_pollutant
        assert airQualityIndex.compositePollutantsArray[i][2] == expected_result


# def test_initializePollutants():


# def test_reinitializePollutants():


# def test_getPollutantsArray():


# def test_getCompositePollutantsArray():
