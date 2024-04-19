import pytest
import math
from src.sensors import readSensors


@pytest.mark.parametrize(
    "PMTwoPointFiveInput, PMTwoPointFiveExpected",
    [
        pytest.param(5.5, 6, id="Dirty value is 5.5"),
        pytest.param(0.5, 1, id="Dirty value is 0.5"),
    ],
)
def test_readPMTwoPointFive(mocker, PMTwoPointFiveInput, PMTwoPointFiveExpected):
    mocker.patch.object(readSensors.sensors,"sensePMTwoPointFive", return_value=PMTwoPointFiveInput)
    result = readSensors.readPMTwoPointFive()
    assert result == PMTwoPointFiveExpected


@pytest.mark.parametrize(
    "PMTenInput, PMTenExpected",
    [
        pytest.param(10.5, 11, id="Dirty value is 10.5"),
    ],
)
def test_readPMTen(mocker, PMTenInput, PMTenExpected):
    mocker.patch.object(readSensors.sensors,"sensePMTen", return_value=PMTenInput)
    result = readSensors.readPMTen()
    assert result == PMTenExpected


@pytest.mark.parametrize(
    "sulfurDioxideInput, sulfurDioxideExpected",
    [
        pytest.param(2.5, 3, id="Dirty value is 2.5"),
    ],
)
def test_readSulfurDioxide(mocker, sulfurDioxideInput, sulfurDioxideExpected):
    mocker.patch.object(readSensors.sensors,"senseSulfurDioxide", return_value=sulfurDioxideInput)
    result = readSensors.readSulfurDioxide()
    assert result == sulfurDioxideExpected


@pytest.mark.parametrize(
    "nitrogenDioxideInput, nitrogenDioxideExpected",
    [
        pytest.param(1.8, 2, id="Dirty value is 1.8"),
    ],
)
def test_readNitrogenDioxide(mocker, nitrogenDioxideInput, nitrogenDioxideExpected):
    mocker.patch.object(readSensors.sensors, "senseNitrogenDioxide", return_value=nitrogenDioxideInput)
    result = readSensors.readNitrogenDioxide()
    assert result == nitrogenDioxideExpected


@pytest.mark.parametrize(
    "ozoneInput, ozoneExpected",
    [
        pytest.param(0.05, 1, id="Dirty value is 0.05"),
    ],
)
def test_readOzone(mocker, ozoneInput, ozoneExpected):
    mocker.patch.object(readSensors.sensors,"senseOzone", return_value=ozoneInput)
    result = readSensors.readOzone()
    assert result == ozoneExpected


@pytest.mark.parametrize(
    "carbonMonoxideInput, carbonMonoxideExpected",
    [
        pytest.param(0.3, 1, id="Dirty value is 0.3"),
    ],
)
def test_readCarbonMonoxide(mocker, carbonMonoxideInput, carbonMonoxideExpected):
    mocker.patch.object(readSensors.sensors,"senseCarbonMonoxide", return_value=carbonMonoxideInput)
    result = readSensors.readCarbonMonoxide()
    assert result == carbonMonoxideExpected


@pytest.mark.parametrize(
    "windDirectionInput, windDirectionExpected",
    [
        pytest.param(180, "S", id="Dirty value is 180"),
    ],
)
def test_readWindDirection(mocker, windDirectionInput, windDirectionExpected):
    mocker.patch.object(readSensors.sensors,"senseWindDirection", return_value=windDirectionInput)
    result = readSensors.readWindDirection()
    assert result == windDirectionExpected


@pytest.mark.parametrize(
    "windSpeedInput, windSpeedExpected",
    [
        pytest.param(10.5, 11, id="Dirty value is 10.5"),
    ],
)
def test_readWindSpeed(mocker, windSpeedInput, windSpeedExpected):
    mocker.patch.object(readSensors.sensors,"senseWindSpeed", return_value=windSpeedInput)
    result = readSensors.readWindSpeed()
    assert result == windSpeedExpected


@pytest.mark.parametrize(
    "precipitationTypeInput, precipitationTypeExpected",
    [
        pytest.param("rain", "rain", id="Dirty value is rain"),
    ],
)
def test_readPrecipitationType(mocker, precipitationTypeInput, precipitationTypeExpected):
    mocker.patch.object(readSensors.sensors,"sensePrecipitationType", return_value=precipitationTypeInput)
    result = readSensors.readPrecipitationType()
    assert result == precipitationTypeExpected


@pytest.mark.parametrize(
    "precipitationAmountInput, precipitationAmountExpected",
    [
        pytest.param(5, 5, id="Dirty value is 5"),
    ],
)
def test_readPrecipitationAmount(mocker, precipitationAmountInput, precipitationAmountExpected):
    mocker.patch.object(readSensors.rand,"triangular", return_value=precipitationAmountInput)
    result = readSensors.readPrecipitationAmount()
    assert result == precipitationAmountExpected