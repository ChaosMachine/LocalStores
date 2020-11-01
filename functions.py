from geopy.geocoders import Nominatim

def get_location(city):
    geolocator = Nominatim(user_agent="Enefso")
    location = geolocator.geocode(city)
    longitude = location.longitude
    latitude = location.latitude
    return longitude,latitude