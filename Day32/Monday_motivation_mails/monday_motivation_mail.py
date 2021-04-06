import smtplib
import datetime as dt
import random

my_email = "akashbm08@gmail.com"
password = "Akya@101320"
today_day = dt.datetime.now()
print(today_day.weekday())

if int(today_day.weekday()) == 0:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
    with smtplib.SMTP("smtp.gmail.com") as g_connection:
        #g_connection = smtplib.SMTP("smtp.gmail.com")
        g_connection.starttls()
        g_connection.login(user="akashbm08@gmail.com", password="Akya@101320")
        g_connection.sendmail(from_addr="akashbm08@gmail.com",
                              to_addrs="akashmali8599@gmail.com",
                              msg=f"Subject:Monday Motivation\n\n{random.choice(data)}")
