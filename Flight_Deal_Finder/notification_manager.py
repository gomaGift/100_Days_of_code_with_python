from twilio.rest import Client
import os
from flight_data import FlightData

ACC_SID = 'AC00bb47cb2ac49df6b4142bbfb94bd11e'
AUTH_TOKEN = '6a0d56836734c22f14f313efaa5f2130'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data: FlightData):
        # Set environment variables for your credentials
        # Read more at http://twil.io/secure
        account_sid = "AC00bb47cb2ac49df6b4142bbfb94bd11e"
        auth_token = '6a0d56836734c22f14f313efaa5f2130'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Cheap deal alert! for only £{flight_data.price},\n"
                 f"fly from {flight_data.origin_city} - {flight_data.origin_airport} "
                 f"to {flight_data.destination_city} - {flight_data.destination_airport}\n"
                 f"from {flight_data.out_date} to {flight_data.return_date}",
            from_="+16516612493",
            to="+260976693699"
        )

        print(message.sid)
