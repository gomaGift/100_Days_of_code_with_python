import smtplib

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login()