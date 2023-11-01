import requests

from Flight_Deal_Finder.flight_data import FlightData
from data_manager import DataManager
import datetime as dt

FLIGHT_SEARCH_URL = 'https://api.tequila.kiwi.com/locations/query'
API_KEY = "5N-TWBIcS77Itdr2abWuvc3pknBgYCBI"
FLIGHT_DATA_URL = 'https://api.tequila.kiwi.com/v2/search'
FLIGHT_DATA_API = '5N-TWBIcS77Itdr2abWuvc3pknBgYCBI'
DATE = dt.datetime.now()
from_d = DATE + dt.timedelta(days=1)
add_days = DATE + dt.timedelta(days=6 * 30)
DATE_FROM = from_d.strftime('%d/%m/%Y')
DATE_TO = add_days.strftime('%d/%m/%Y')


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data: DataManager):
        self.flight_data = data


    def search_iata_codes(self):
        # method is responsible for searching the iata codes for the respective destinations
        header = {
            "apikey": API_KEY,
        }

        parameters = {
            'term': '',
        }

        for city_data in self.flight_data:
            parameters['term'] = city_data['city']
            response = requests.get(url=FLIGHT_SEARCH_URL, headers=header, params=parameters).json()
            city_code = response['locations'][0]['code']
            city_data['iataCode'] = city_code

    def check_flights(self, origin_city_code, destination_city_code ):
        headers = {"apikey": FLIGHT_DATA_API}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=FLIGHT_DATA_URL,
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            query['max_stop_o']

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            stop_overs = 0,
            via_city = 'via_city'
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
