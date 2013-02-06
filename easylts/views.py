from flask.ext.mongoengine.wtf import model_form
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from easylts.models import BusStop

bus_stops = Blueprint('bus_stops', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        bus_stops = BusStop.objects.all()
        return render_template('bus_stops/list.html', bus_stops=bus_stops)


class DetailView(MethodView):

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('bus_stops/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        return render_template('bus_stops/detail.html', **context)

# Register the urls
bus_stops.add_url_rule('/', view_func=ListView.as_view('list'))
bus_stops.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
