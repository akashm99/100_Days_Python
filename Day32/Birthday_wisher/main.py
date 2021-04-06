import datetime as dt
import pandas as pd
import random
import smtplib

data = pd.read_csv("birthdays.csv")
month = dt.datetime.now().month
day = dt.datetime.now().day

my_email = "akashbm08@gmail.com"
password = ""
r_letter = f"letter_{random.randint(1,3)}.txt"

for rows in data.iterrows():
    target_day = rows[1]["day"]
    target_month = rows[1]["month"]
    if target_day == day and target_month == month:
        target_email = rows[1]["email"]
        target_name = rows[1]["name"]
        with open(f"letter_templates/{r_letter}") as letter:
            letter_contents = letter.read()
            new_letter = letter_contents.replace("[NAME]", target_name)

        with smtplib.SMTP("smtp.gmail.com") as g_connection:
            # g_connection = smtplib.SMTP("smtp.gmail.com")
            g_connection.starttls()
            g_connection.login(user=my_email, password=password)
            g_connection.sendmail(from_addr=my_email,
                                  to_addrs=target_email,
                                  msg=f"Subject:Happy BirthDay\n\n{new_letter}")


# today = dt.datetime.now()
# today_tuple = (today.day, today.month)
# data = pd.read_csv("birthdays.csv")
# bday_dict = {(data_row.month, data_row.day): data_row for (index,data_row) in data.iterrows()}
# if today_tuple in bday_dict:
#     name = bday_dict[today_tuple]["name"]
#     email = bday_dict[today_tuple]["email"]





