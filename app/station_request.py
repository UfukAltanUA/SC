from requests import get
from app import app, cache

@cache.cached(timeout = app.config['TIMEOUT'])
def get_stations():
    return get(app.config['LOCATION_SERVICE_URL'] + '/station/yhtStations').json()
