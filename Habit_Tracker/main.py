import requests
import  datetime as dt

TOKEN = 'mpatsokjdk'
USERNAME = 'mpatso'
pixela_endpoint = 'https://pixe.la/v1/users'

parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

HEADERS = {
    'X-USER-TOKEN': TOKEN
}
GRAPH_ID = 'graph01'
graph_parameters = {
    'id': GRAPH_ID,
    'name': 'coding_graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

# response_graph = requests.post(url=graph_endpoint, json=graph_parameters, headers=HEADERS)
# print(response_graph.text)
today = dt.datetime.now()
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_parameters = {
    'date': '20230104',
    'quantity': '240'
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=HEADERS)
# print(pixel_response.text)
