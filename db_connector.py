from pymongo import Connection
import urllib
import json
import pprint
import yaml

connection = Connection('localhost', 27017)
db = connection.test_database
db.shelters.drop()
shelters_model = db.shelters
URL2 = "http://lafayette.otvia.com/packet/json/allshelters"

if __name__ == "__main__":
    allshelters = urllib.urlopen(URL2)
    shelters = yaml.load(allshelters)

    for shelter in shelters['ShelterArray']:
        stuff = shelter['Shelter']
        sh = {"shelter_id": stuff['ShelterId'],
                "name": stuff['ShelterName'],
                "latitude": stuff['Latitude']/100000.0,
                "longitude": -stuff['Longitude']/100000.0}

        # print sh
        shelters_model.insert(sh)
        route_ids = stuff['routeIDs']
        for i in route_ids:
            print i
