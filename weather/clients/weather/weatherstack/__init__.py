import requests

import clients.weather.models as models

def get_weather(city):
    access_key = '4a525fe4deab4bf629b47641eb9afa01'
    response = requests.get(
        'http://api.weatherstack.com/current',
        params={
        }
    )

    return models.Weather(temperature=273.15)
