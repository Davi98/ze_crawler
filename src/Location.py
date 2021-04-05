import requests
import urllib.parse

class Location:

    def __init__(self,street_name,zip_code):
        self.street_name = street_name
        self.zip_code = zip_code
        self.address = f"{street_name},{zip_code}"
        self.url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(self.address) +'?format=json'

    def get_lat_log(self):
        response = requests.get(self.url).json()
        return response[0]["lat"],response[0]["lon"]