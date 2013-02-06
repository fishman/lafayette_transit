from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('easylts.config')

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()


def register_blueprints(app):
    # Prevents circular imports
    from easylts.views import bus_stops
    app.register_blueprint(bus_stops)

register_blueprints(app)
