import pytest
from flask.testing import FlaskClient
import src.weather_api.__init__ as init

# fixture to create a flask test client 
@pytest.fixture
def client() -> FlaskClient:
    init.app.testing = True
    return init.app.test_client()

# asynchronous test to test /wind endpoint
@pytest.mark.asyncio
async def test_get_wind(client: FlaskClient):
    response = await client.get('/wind')
    assert response.status_code == 200
    data = await response.get_json()
    assert 'HourlyWind' in data

# asynchronous test to test /precipitation endpoint
@pytest.mark.asyncio
async def test_get_precipitation(client: FlaskClient):
    response = await client.get('/precipitation')
    assert response.status_code == 200
    data = await response.get_json()
    assert 'HourlyPrecipitation' in data

# asynchronous test to test /aqi endpoint
@pytest.mark.asyncio
async def test_get_aqi(client: FlaskClient):
    response = await client.get('/aqi')
    assert response.status_code == 200
    data = await response.get_json()
    assert 'HourlyAQI' in data

