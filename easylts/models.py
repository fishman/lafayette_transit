import datetime
from flask import url_for
from easylts import db


class BusStop(db.Document):
    route_id = db.IntField()
    shelter_id = db.IntField()
    name = db.StringField(max_length=255, required=True)
    point = db.GeoPointField()
