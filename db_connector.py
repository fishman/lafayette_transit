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


class BusStop(EmbeddedDocument):
    shelter_id = IntField()
    name = StringField()
    point = GeoPointField()


class Route(Document):
    route_id = IntField()
    bus_stops = ListField(EmbeddedDocumentField(BusStop))

if __name__ == "__main__":
    allshelters = urllib.urlopen(URL2)
    shelters = yaml.load(allshelters)

    for shelter in shelters['ShelterArray']:
        stuff = shelter['Shelter']

        stop = BusStop(shelter_id=stuff['ShelterId'], name=stuff['ShelterName'])

        stop.point = [stuff['Latitude']/100000.0, -stuff['Longitude']/100000.0]
        route_ids = stuff['routeIDs']
        for i in route_ids:
            routes = Route.objects(route_id=i)
            if len(routes) > 0:
                route = routes[0]
            else:
                route = Route(route_id=i)

            route.bus_stops.append(stop)
            route.save()

    print Route.objects

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
