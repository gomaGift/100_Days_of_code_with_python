import datetime
import smtplib
import time
import requests

LATITUDE = -15.387526
LONGITUDE = 28.322817


def compare_proximity():
    result = requests.get(url='http://api.open-notify.org/iss-now.json')
    result.raise_for_status()

    iss_latitude = float(result.json()['iss_position']['latitude'])
    iss_longitude = float(result.json()['iss_position']['longitude'])

    return abs(LATITUDE - iss_latitude) <= 5 and abs(LONGITUDE - iss_longitude) <= 5


def is_dark():
    parameters = {
        'lat': LATITUDE,
        'lng': LONGITUDE,
        'formatted': 0,
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_time = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_time = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour
    return  sunset_time <= time_now or time_now <= sunrise_time


email = "gomagiftk01@gmail.com"
password = 'hbxelnuzetwllvsv'
# If the ISS is close to my current position

if compare_proximity() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="giftgoma@icloud.com",
                            msg=f"Subject:Iss Overhead\n\nlook up")

