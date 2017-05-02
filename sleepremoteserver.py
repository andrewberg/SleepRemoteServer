#!/usr/bin/env python

from py_irsend import irsend
from flask import Flask
app = Flask(__name__)

def send_power_signal():
    irsend.send_once('HDX', ['KEY_POWER'])


@app.route("/signal")
def send_signal():
    send_power_signal()
    return "Signal sent!"

@app.route("/connect")
def send_connect():
    return "We are connected!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')