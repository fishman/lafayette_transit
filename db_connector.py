from pymongo import Connection
import urllib
import json
import pprint
import yaml

connection = Connection('localhost', 27017)
db = connection.test_database
posts = db.posts
URL2 = "http://lafayette.otvia.com/packet/json/allshelters"

if __name__ == "__main__":
    allshelters = urllib.urlopen(URL2)
    shelters = yaml.load(allshelters)

    for shelter in shelters['ShelterArray']:
        sh = {"shelter_id": shelter['Shelter']['ShelterId'],
                "name": shelter['Shelter']['ShelterName'],
                "latitude": shelter['Shelter']['Latitude'],
                "longitude": shelter['Shelter']['Longitude']}
        print sh
