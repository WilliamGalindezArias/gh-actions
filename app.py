import logging
from flask import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("Main Request: SUCCESS")
    return "Hello World!"


@app.route("/status")
def status():
    response = app.response_class(
        response = json.dumps({"result": "OK - Healthy"}),
        status = 200,
        mimetype = "application/json"
    )
    app.logger.info("Status Requested")
    return response


@app.route("/metrics")
def metrics():

    response = app.response_class(
        response=json.dumps({"status":"success",
                             "code":0,
                             "data":{"UserCount":140,
                                     "UserCountActive":23}}),
                            status=200,
                            mimetype="application/json"
                            )

    app.logger.info("Metrics Requested")

    return response


if __name__ == "__main__":
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app.run(host='0.0.0.0')
