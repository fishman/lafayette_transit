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


class BusStop(Document):
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

    # for shelter in shelters['ShelterArray']:
    #     stuff = shelter['Shelter']
    #     sh = {"shelter_id": stuff['ShelterId'],
    #             "name": stuff['ShelterName'],
    #             "latitude": stuff['Latitude']/100000.0,
    #             "longitude": -stuff['Longitude']/100000.0}

    #     # print sh
    #     shelters_model.insert(sh)
    #     route_ids = stuff['routeIDs']

    #     for i in route_ids:


    #         print i
