import requests

my_api = 'a2ea3727642a258752c5fe1699506311'

wmap_end_point = 'https://api.openweathermap.org/data/2.5/weather'

parameters = {
    'lat': -15.387526,
    'lon': 28.322817,
    'appid': my_api,
}

response = requests.get(wmap_end_point, params=parameters)
print(response.json())