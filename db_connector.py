from pymongo import Connection
from mongoengine import *
import urllib
import json
import pprint
import yaml

# connection = Connection('localhost', 27017)
# db = connection.test_database
# db.shelters.drop()
# db.routes.drop()
# shelters_model = db.shelters
# routes_model = db.routes

connect('test_database')

URL2 = "http://lafayette.otvia.com/packet/json/allshelters"
allshelters = urllib.urlopen(URL2)
shelters = yaml.load(allshelters)

# URL2 = "http://lafayette.otvia.com/packet/json/route"
# allroutes = urllib.urlopen(URL2)
# routes = yaml.load(allroutes)


class BusStop(Document):
    # kml_id
    route_id = IntField()
    shelter_id = IntField()
    name = StringField()
    point = GeoPointField()


if __name__ == "__main__":
    allshelters = urllib.urlopen(URL2)
    shelters = yaml.load(allshelters)

    for shelter in shelters['ShelterArray']:
        stuff = shelter['Shelter']

        route_ids = stuff['routeIDs']
        for i in route_ids:
            stop = BusStop(shelter_id=stuff['ShelterId'], name=stuff['ShelterName'])
            stop.point = [stuff['Latitude']/100000.0, -stuff['Longitude']/100000.0]
            stop.route_id = i
            stop.save()

    print BusStop.objects
