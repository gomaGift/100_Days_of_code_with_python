import random
import smtplib
import datetime as dt

email = "gomagiftk01@gmail.com"
password = 'hbxelnuzetwllvsv'

now = dt.datetime.now()
day = now.weekday()
if day == 4:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)

        quote = random.choice(quotes_list)
        connection.sendmail(from_addr=email, to_addrs="giftian.kg@gmail.com",
                            msg=f"Subject:Quote of the day\n\n{quote}")
