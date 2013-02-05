#!/usr/bin/env python

from flask import Flask
from flask import render_template
import urllib
import json
import pprint
import yaml

app = Flask(__name__)
URL2 = "http://lafayette.otvia.com/packet/json/allshelters"


# BusStop.objects(point__within_distance=([30.21638, -92.01983], (remaining: 0.01))

googleResponse = urllib.urlopen(URL2)
# jsonResponse = json.loads(googleResponse.read())
# pprint.pprint(jsonResponse)
# pprint.pprint(yaml.load(googleResponse))

URL2 = "http://lafayette.otvia.com/packet/json/shelter?routes=41,43,44,45,46,47,48,49,50,51,52,53,54,42&lastShelterHttpRequestTime=1357503205449"
googleResponse = urllib.urlopen(URL2)
# pprint.pprint(yaml.load(googleResponse))


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
