import pytest
from src.weather_api import airQualityIndex as aqi


@pytest.mark.parametrize(
    "pollutant",
    [
        pytest.param(0, id="Zeros"),
        pytest.param(1.1, id="Floats"),
    ],
)
def test_buildPollutantsArray(mocker, pollutant):
    mocker.patch.object(aqi.sensors, "readPMTwoPointFive", return_value=pollutant)
    mocker.patch.object(aqi.sensors, "readPMTen", return_value=pollutant)
    mocker.patch.object(aqi.sensors, "readCarbonMonoxide", return_value=pollutant)
    mocker.patch.object(aqi.sensors, "readNitrogenDioxide", return_value=pollutant)
    mocker.patch.object(aqi.sensors, "readSulfurDioxide", return_value=pollutant)
    mocker.patch.object(aqi.sensors, "readOzone", return_value=pollutant)

    aqi.buildPollutantsArray()

    for i in range(24):
        for j in range(6):
            assert aqi.pollutantsArray[i][j] == pollutant


@pytest.mark.parametrize(
    "first_pollutant, second_pollutant, expected_result",
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
        aqi.pollutantsArray[i][0] = first_pollutant
        aqi.pollutantsArray[i][1] = first_pollutant
        aqi.pollutantsArray[i][2] = second_pollutant
        aqi.pollutantsArray[i][3] = second_pollutant
        aqi.pollutantsArray[i][4] = second_pollutant
        aqi.pollutantsArray[i][5] = second_pollutant

    aqi.calculateCompositePollutants()
    for i in range(24):
        assert aqi.pollutantsCompositeArray[i][0] == first_pollutant
        assert aqi.pollutantsCompositeArray[i][1] == second_pollutant
        assert aqi.pollutantsCompositeArray[i][2] == expected_result


@pytest.mark.parametrize(
    "pollutant, called_bool",
    [
        pytest.param(0, True, id="EmptyArray"),
        pytest.param(1.1, False, id="FilledArray"),
    ],
)
def test_initializePollutants(mocker, pollutant, called_bool):
    mockedArrayBuilder = mocker.patch.object(aqi, "buildPollutantsArray")
    mockedArrayBuilder2 = mocker.patch.object(aqi, "calculateCompositePollutants")
    aqi.pollutantsArray[0][0] = pollutant
    if called_bool:
        aqi.initializePollutants()
        mockedArrayBuilder.assert_called_once()
        mockedArrayBuilder2.assert_called_once()
    else:
        aqi.initializePollutants()
        mockedArrayBuilder.assert_not_called()
        mockedArrayBuilder2.assert_not_called()


def test_reinitializePollutants(mocker):
    mockedArrayBuilder = mocker.patch.object(aqi, "buildPollutantsArray")
    mockedArrayBuilder2 = mocker.patch.object(aqi, "calculateCompositePollutants")
    aqi.reinitializePollutants()
    mockedArrayBuilder.assert_called_once()
    mockedArrayBuilder2.assert_called_once()


def test_getPollutantsArray(mocker):
    mockedInitialize = mocker.patch.object(aqi, "initializePollutants")

    for i in range(24):
        aqi.pollutantsArray[i][0] = 1.1
        aqi.pollutantsArray[i][1] = 1.1
        aqi.pollutantsArray[i][2] = 1.1
        aqi.pollutantsArray[i][3] = 1.1
        aqi.pollutantsArray[i][4] = 1.1
        aqi.pollutantsArray[i][5] = 1.1
    returnedArray = aqi.getPollutantsArray()
    for i in range(24):
        assert returnedArray[i][0] == 1.1
        assert returnedArray[i][1] == 1.1
        assert returnedArray[i][2] == 1.1
        assert returnedArray[i][3] == 1.1
        assert returnedArray[i][4] == 1.1
        assert returnedArray[i][5] == 1.1
    mockedInitialize.assert_called_once()


def test_getCompositePollutantsArray(mocker):
    mockedInitialize = mocker.patch.object(aqi, "initializePollutants")

    for i in range(24):
        aqi.pollutantsCompositeArray[i][0] = 1.1
        aqi.pollutantsCompositeArray[i][1] = 1.1
        aqi.pollutantsCompositeArray[i][2] = 1.1
    returnedArray = aqi.getCompositePollutantsArray()
    for i in range(24):
        assert returnedArray[i][0] == 1.1
        assert returnedArray[i][1] == 1.1
        assert returnedArray[i][2] == 1.1
    mockedInitialize.assert_called_once()
