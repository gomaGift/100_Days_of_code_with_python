import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_url = 'https://api.sheety.co/8031c5d9b96d5933fcc01dd30608bc8d/flightDeals/prices'
        self.data = requests.get(url=self.get_url).json()['prices']

    def update_sheet(self):
        # method is responsible for filling the iata fields of the destinations with their respective
        # values

        parameter = {
            'price': {
                'iataCode': ' '
            }
        }
        for destination in self.data:
            put_url = f'https://api.sheety.co/8031c5d9b96d5933fcc01dd30608bc8d/flightDeals/prices/{destination["id"]}'

            parameter['price']['iataCode'] = destination['iataCode']
            requests.put(url=put_url, json=parameter)



