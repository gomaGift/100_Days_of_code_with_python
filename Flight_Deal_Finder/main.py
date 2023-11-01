# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
CITY = 'london'
CITY_ORIGIN_CODE = 'LUN'
FLIGHT_BUDGET = 90


data_manager = DataManager()
sheet_data = data_manager.data

flight_search = FlightSearch(sheet_data)
flight_search.search_iata_codes()

data_manager.data = flight_search.flight_data

data_manager.update_sheet()

for destination in data_manager.data:
    dest_code = destination['iataCode']
    flight  = flight_search.check_flights(origin_city_code=CITY_ORIGIN_CODE, destination_city_code=dest_code)
    if flight.price < FLIGHT_BUDGET:
        notification = NotificationManager(flight)





