from quart import Quart, jsonify, request

from src.weather_api import precipitation as precipitation
from src.weather_api import wind as wind
from src.weather_api import airQualityIndex as aqi

app = Quart(__name__)


@app.get("/wind")
async def getWind():
    return jsonify(HourlyWind=wind.getWindArray())


@app.get("/precipitation")
async def getPrecipitation():
    return jsonify(HourlyPrecipitation=precipitation.getPrecipitationArray())


# later on I want this to return either full or composite based on a query param
@app.get("/aqi")
async def getAQI():
    return jsonify(HourlyAQI=aqi.getPollutantsArray())


def run() -> None:
    app.run(host="0.0.0.0", port=80)
