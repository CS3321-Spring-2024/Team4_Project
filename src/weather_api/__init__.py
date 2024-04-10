from quart import Quart, jsonify, request

import precipitation as precipitation
import wind as wind
import airQualityIndex as aqi

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
    app.run()
