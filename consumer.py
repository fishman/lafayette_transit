#!/usr/bin/env python

from flask import Flask
import urllib
import json
import pprint
import yaml
from pymongo import Connection

app = Flask(__name__)
URL2 = "http://lafayette.otvia.com/packet/json/allshelters"



googleResponse = urllib.urlopen(URL2)
# jsonResponse = json.loads(googleResponse.read())
# pprint.pprint(jsonResponse)
pprint.pprint(yaml.load(googleResponse))

URL2 = "http://lafayette.otvia.com/packet/json/shelter?routes=41,43,44,45,46,47,48,49,50,51,52,53,54,42&lastShelterHttpRequestTime=1357503205449"
googleResponse = urllib.urlopen(URL2)
pprint.pprint(yaml.load(googleResponse))


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

# opener = urllib2.build_opener()
