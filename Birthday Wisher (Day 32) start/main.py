##################### Extra Hard Starting Project ######################
import random

import pandas as pd
import datetime as dt
import smtplib
import os

email = "gomagiftk01@gmail.com"
password = 'hbxelnuzetwllvsv'
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

for loved_one in birthdays_dict:
    if loved_one['day'] == day and loved_one['month'] == month:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
        random_letter = random.choice(os.listdir("./letter_templates"))
        with open(os.path.join("./letter_templates", random_letter), 'r') as attachment:
            letter = attachment.read()
            birthday_wish = letter.replace("[NAME]", f"{loved_one['name']}")
        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=f"{loved_one['email']}",
                                msg=f"Subject:Birth Day Wishes\n\n{birthday_wish}")
