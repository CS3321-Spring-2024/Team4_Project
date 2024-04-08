from quart import Quart, jsonify, request

app = Quart(__name__)


@app.get("/example")
async def example():
    return jsonify(["a", "b"])

@app.get("/wind")
async def wind():
    return jsonify(["a", "b"])

@app.get("/precipitation")
async def precipitation():
    return jsonify(["30% Rain"])


@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}


def run() -> None:
    app.run()
